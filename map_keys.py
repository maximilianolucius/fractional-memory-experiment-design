import re
import subprocess
import sys
import os

def normalize_author(author):
    """Normalize author string for comparison."""
    author = author.lower()
    author = re.sub(r'\s+', ' ', author)
    return author.strip()

def normalize_title(title):
    """Normalize title string for comparison."""
    title = title.lower()
    title = re.sub(r'\s+', ' ', title)
    return title.strip()

def parse_bibtex_file(filepath):
    """Parse a BibTeX file and return a dict mapping key to (author, title, year)."""
    mapping = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return mapping
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
        # Now, we want to extract the fields. We'll look for the whole entry until the matching '}'
        # We'll find the matching brace for the outer braces.
        brace_count = 0
        in_brace = False
        end_idx = -1
        for i, ch in enumerate(block):
            if ch == '{':
                if not in_brace:
                    in_brace = True
                brace_count += 1
            elif ch == '}':
                brace_count -= 1
                if brace_count == 0 and in_brace:
                    end_idx = i
                    break
        if end_idx == -1:
            # Fallback: take the rest of the block
            field_str = block[brace_open+1:]
        else:
            field_str = block[brace_open+1:end_idx]
        # Now parse fields: look for patterns like author = { ... }, title = { ... }, year = { ... }
        fields = {}
        # We'll use a regex to match each field: (\w+)\s*=\s*{([^}]*)}
        # This assumes no nested braces.
        field_pattern = re.compile(r'(\w+)\s*=\s*{([^}]*)}')
        for match in field_pattern.finditer(field_str):
            field_name = match.group(1).lower()
            field_value = match.group(2).strip()
            fields[field_name] = field_value
        author = fields.get('author', '')
        title = fields.get('title', '')
        year = fields.get('year', '')
        mapping[key] = (author, title, year)
    return mapping

def main():
    # Step 1: Parse the new bibliography (the one we generated from markdown)
    new_bib_path = 'paper/bibliography.bib'
    new_mapping = parse_bibtex_file(new_bib_path)
    print(f"Parsed {len(new_mapping)} entries from new bibliography.")
    
    # Step 2: Get original bibliography from git
    try:
        original_bib_content = subprocess.check_output(
            ['git', 'show', 'HEAD:paper/bibliography.bib'],
            stderr=subprocess.DEVNULL,
            text=True
        )
    except subprocess.CalledProcessError:
        print("Could not retrieve original bibliography from git. Proceeding without key replacement.")
        original_bib_content = ""
    
    original_mapping = {}
    if original_bib_content:
        # Write the original content to a temporary file and parse it
        with open('temp_original.bib', 'w', encoding='utf-8') as f:
            f.write(original_bib_content)
        original_mapping = parse_bibtex_file('temp_original.bib')
        os.remove('temp_original.bib')
        print(f"Parsed {len(original_mapping)} entries from original bibliography.")
    else:
        print("No original bibliography found.")
    
    # Step 3: Build mapping from original keys to new keys
    # We'll create a list of new entries with normalized author, title, year for matching
    new_entries_norm = []
    for key, (author, title, year) in new_mapping.items():
        norm_author = normalize_author(author)
        norm_title = normalize_title(title)
        new_entries_norm.append({
            'key': key,
            'author': norm_author,
            'title': norm_title,
            'year': year
        })
    
    # Build a dictionary from (normalized_author, normalized_title, year) to new key
    new_map = {}
    for entry in new_entries_norm:
        key_tuple = (entry['author'], entry['title'], entry['year'])
        # If there are duplicates, we take the first one
        if key_tuple not in new_map:
            new_map[key_tuple] = entry['key']
    
    old_to_new = {}
    for old_key, (author, title, year) in original_mapping.items():
        norm_author = normalize_author(author)
        norm_title = normalize_title(title)
        year_str = year  # already a string
        key_tuple = (norm_author, norm_title, year_str)
        new_key = new_map.get(key_tuple)
        if new_key:
            old_to_new[old_key] = new_key
        else:
            print(f"Warning: No matching new entry found for original key '{old_key}'")
            print(f"  Author: {author}")
            print(f"  Title: {title}")
            print(f"  Year: {year}")
    
    print(f"Created mapping for {len(old_to_new)} original keys to new keys.")
    if old_to_new:
        print("Mapping:", old_to_new)
    
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