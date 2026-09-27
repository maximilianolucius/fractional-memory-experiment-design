import re
import subprocess
import sys
import os

def normalize_author(author):
    """Normalize author string for comparison."""
    author = author.lower()
    # Replace '&' with 'and', remove extra spaces
    author = re.sub(r'\s+', ' ', author)
    return author.strip()

def normalize_title(title):
    """Normalize title string for comparison."""
    title = title.lower()
    title = re.sub(r'\s+', ' ', title)
    return title.strip()

def parse_markdown_reference(citation):
    """
    Parse a citation string from the markdown.
    Returns a dict with keys: author, year, title.
    """
    # Extract year: look for (yyyy)
    year_match = re.search(r'\((\d{4})\)', citation)
    if not year_match:
        return None
    year = year_match.group(1)
    
    # Author: everything before the year, remove trailing dot and spaces
    author_part = citation[:year_match.start()].strip()
    if author_part.endswith('.'):
        author = author_part[:-1].strip()
    else:
        author = author_part
    
    # The part after the year
    after_year = citation[year_match.end():].strip()
    # Remove leading dot and space if present
    if after_year.startswith('. '):
        after_year = after_year[2:]
    elif after_year.startswith('.'):
        after_year = after_year[1:]
    
    # Now try to extract the title: look for the first asterisk (which starts the journal title in italics)
    asterisk_idx = after_year.find('*')
    if asterisk_idx != -1:
        title = after_year[:asterisk_idx].strip()
        # Remove trailing dot if present
        if title.endswith('.'):
            title = title[:-1].strip()
    else:
        # If no asterisk, take the whole string as title (but remove trailing dot)
        title = after_year.strip()
        if title.endswith('.'):
            title = title[:-1].strip()
    
    return {
        'author': author,
        'year': year,
        'title': title
    }

def parse_bibtex(content):
    """Parse BibTeX content into a dict: key -> (author, title, year)."""
    mapping = {}
    # Split by '@' and process each block
    blocks = re.split(r'\n@', content)
    for block in blocks[1:]:  # Skip the first empty part
        block = block.strip()
        if not block:
            continue
        # Extract the key: everything after '{' until the first comma
        brace_open = block.find('{')
        if brace_open == -1:
            continue
        after_brace = block[brace_open+1:]
        comma = after_brace.find(',')
        if comma == -1:
            continue
        key = after_brace[:comma].strip()
        # Now extract fields: we look for author, title, year
        # We'll use a simple regex to capture fields like author = { ... }
        # This assumes no nested braces.
        field_pattern = re.compile(r'(\w+)\s*=\s*{([^}]*)}')
        fields = {}
        for match in field_pattern.finditer(after_brace):
            field_name = match.group(1).lower()
            field_value = match.group(2).strip()
            fields[field_name] = field_value
        author = fields.get('author', '')
        title = fields.get('title', '')
        year = fields.get('year', '')
        mapping[key] = (author, title, year)
    return mapping

def main():
    # Step 1: Read current bibliography (the one we want to use)
    current_bib_path = 'paper/bibliography.bib'
    with open(current_bib_path, 'r', encoding='utf-8') as f:
        current_content = f.read()
    current_map = parse_bibtex(current_content)
    print(f"Parsed {len(current_map)} entries from current bibliography.")
    
    # Step 2: Read original bibliography from git
    try:
        original_content = subprocess.check_output(
            ['git', 'show', 'HEAD:paper/bibliography.bib'],
            stderr=subprocess.DEVNULL,
            text=True
        )
    except subprocess.CalledProcessError:
        print("Could not retrieve original bibliography from git. Exiting.")
        sys.exit(1)
    original_map = parse_bibtex(original_content)
    print(f"Parsed {len(original_map)} entries from original bibliography.")
    
    # Step 3: Build mapping from original keys to current keys
    # Normalize current entries for matching
    current_norm = {}
    for key, (author, title, year) in current_map.items():
        norm_author = normalize_author(author)
        norm_title = normalize_title(title)
        # Use tuple as key
        key_tuple = (norm_author, norm_title, year)
        # If there are duplicates, we take the first one (should not happen)
        if key_tuple not in current_norm:
            current_norm[key_tuple] = key
    
    old_to_new = {}
    for old_key, (author, title, year) in original_map.items():
        norm_author = normalize_author(author)
        norm_title = normalize_title(title)
        year_str = year  # already string
        key_tuple = (norm_author, norm_title, year_str)
        new_key = current_norm.get(key_tuple)
        if new_key:
            old_to_new[old_key] = new_key
        else:
            print(f"Warning: No matching current entry for original key '{old_key}'")
            print(f"  Author: {author}")
            print(f"  Title: {title}")
            print(f"  Year: {year}")
    
    print(f"Created mapping for {len(old_to_new)} original keys to new keys.")
    if old_to_new:
        print("Sample mapping:", dict(list(old_to_new.items())[:5]))
    
    # Step 4: Update citation keys in .tex files
    for root, dirs, files in os.walk('paper'):
        for file in files:
            if file.endswith('.tex'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Replace each old key with new key
                for old_key, new_key in old_to_new.items():
                    # Use word boundaries to avoid partial matches
                    pattern = r'\b' + re.escape(old_key) + r'\b'
                    content = re.sub(pattern, new_key, content)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
    print("Updated citation keys in .tex files.")
    
    # Step 5: Run bibtex and pdflatex to verify
    print("Running bibtex...")
    result_bibtex = subprocess.run(['bibtex', 'paper/main'], capture_output=True, text=True)
    print(f"BibTeX exit code: {result_bibtex.returncode}")
    if result_bibtex.returncode != 0:
        print("BibTeX stderr:")
        print(result_bibtex.stderr[-500:])
    print("Running pdflatex...")
    result_pdflatex = subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', '-output-directory=paper', 'paper/main.tex'],
        capture_output=True, text=True
    )
    print(f"Pdflatex exit code: {result_pdflatex.returncode}")
    if result_pdflatex.returncode != 0:
        print("Pdflatex stderr:")
        print(result_pdflatex.stderr[-500:])
    else:
        print("LaTeX compilation succeeded.")
    
    # Final count of entries in bibliography.bib
    with open('paper/bibliography.bib', 'r', encoding='utf-8') as f:
        bib_content = f.read()
    num_entries = len(re.findall(r'@\\w+{', bib_content))
    print(f"Number of entries in bibliography.bib: {num_entries}")

if __name__ == '__main__':
    main()