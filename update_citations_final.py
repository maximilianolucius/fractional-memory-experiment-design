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
    Returns a dict with keys: author, year, title, journal, volume, number, pages, doi.
    We focus on author, title, year for matching.
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
    
    # Now try to extract the title
    title = None
    
    # Look for the pattern: . * (dot space star) indicating the start of italic (journal or book title)
    # We want to find the first occurrence of ' . *' or '.*' after the year.
    # We'll search for ' . *' first (space dot space star)
    dot_space_star = after_year.find(' . *')
    dot_star = after_year.find('.*')
    
    # Determine which comes first
    pos = -1
    if dot_space_star != -1 and dot_star != -1:
        pos = min(dot_space_star, dot_star)
    elif dot_space_star != -1:
        pos = dot_space_star
    elif dot_star != -1:
        pos = dot_star
    
    if pos != -1:
        # The title is everything before this position
        title_candidate = after_year[:pos].strip()
        # Remove trailing dot if present
        if title_candidate.endswith('.'):
            title = title_candidate[:-1].strip()
        else:
            title = title_candidate
        # We don't need the rest for now
    else:
        # If we didn't find the pattern, try to look for a book format: *title*
        first_star = after_year.find('*')
        if first_star != -1:
            second_star = after_year.find('*', first_star+1)
            if second_star != -1:
                title = after_year[first_star+1:second_star].strip()
                # Remove trailing dot if present
                if title.endswith('.'):
                    title = title[:-1].strip()
            else:
                # Only one star, maybe the title is until the next period
                # Split by '. ' and take the first part
                parts = after_year.split('. ')
                if parts:
                    title_candidate = parts[0].strip()
                    if title_candidate.endswith('.'):
                        title = title_candidate[:-1].strip()
                    else:
                        title = title_candidate
                else:
                    title = after_year.strip()
        else:
            # No star at all, take the first sentence
            parts = after_year.split('. ')
            if parts:
                title_candidate = parts[0].strip()
                if title_candidate.endswith('.'):
                    title = title_candidate[:-1].strip()
                else:
                    title = title_candidate
            else:
                title = after_year.strip()
    
    # If we still don't have a title, set it to empty string
    if title is None:
        title = ''
    
    return {
        'author': author,
        'year': year,
        'title': title,
        # We don't extract other fields for matching, but we can if needed
        'journal': '',
        'volume': '',
        'number': '',
        'pages': '',
        'doi': ''
    }

def parse_bibtex_simple(content):
    """Parse a BibTeX string into a list of entries with key, author, title, year."""
    entries = []
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
        entry = {
            'key': key,
            'author': fields.get('author', ''),
            'title': fields.get('title', ''),
            'year': fields.get('year', '')
        }
        entries.append(entry)
    return entries

def main():
    # Step 1: Parse the markdown to get new entries
    md_path = '17_BIBLIOGRAPHY.md'
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Split by '\n### [' to get blocks
    blocks = re.split(r'\n### \[', content)
    new_entries = []  # list of dicts with key, author, title, year
    for block in blocks[1:]:  # Skip the first part before first '### ['
        lines = block.split('\n')
        # First line is like "F01] Caputo derivative"
        first_line = lines[0].strip()
        # Extract key: take the part before the first space and remove the trailing ']'
        key = first_line.split()[0].rstrip(']')
        # Find citation line: first non-empty line after the first line that is not a header and contains a year in parentheses
        citation_line = None
        for line in lines[1:]:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith('###'):
                break
            if re.search(r'\(\d{4}\)', stripped) and '.' in stripped:
                citation_line = stripped
                break
        if citation_line is None:
            print(f"Warning: Could not find citation line for key {key}", file=sys.stderr)
            continue
        parsed = parse_markdown_reference(citation_line)
        if parsed is None:
            print(f"Warning: Could not parse citation for key {key}", file=sys.stderr)
            continue
        parsed['key'] = key
        new_entries.append(parsed)
    
    print(f"Parsed {len(new_entries)} new bibliography entries from markdown.")
    # Print first few for debugging
    for i, entry in enumerate(new_entries[:3]):
        print(f"  New entry {i}: key={entry['key']}, author={entry['author']}, title={entry['title']}, year={entry['year']}")
    
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
    
    original_entries = []
    if original_bib_content:
        original_entries = parse_bibtex_simple(original_bib_content)
        print(f"Parsed {len(original_entries)} original bibliography entries.")
        for i, entry in enumerate(original_entries[:3]):
            print(f"  Original entry {i}: key={entry['key']}, author={entry['author']}, title={entry['title']}, year={entry['year']}")
    else:
        print("No original bibliography found.")
    
    # Step 3: Build mapping from original keys to new keys
    # We'll create a list of new entries with normalized author, title, year for matching
    new_entries_norm = []
    for entry in new_entries:
        norm_author = normalize_author(entry['author'])
        norm_title = normalize_title(entry['title'])
        year = entry['year']
        new_entries_norm.append({
            'key': entry['key'],
            'author': norm_author,
            'title': norm_title,
            'year': year
        })
    
    # Build a dictionary from (normalized_author, normalized_title, year) to new key
    # We'll use a list and then do a linear search since the dataset is small
    # But we can also create a dict for O(1) lookup
    new_map = {}
    for entry in new_entries_norm:
        key_tuple = (entry['author'], entry['title'], entry['year'])
        # If there are duplicates, we take the first one
        if key_tuple not in new_map:
            new_map[key_tuple] = entry['key']
    
    old_to_new = {}
    for entry in original_entries:
        norm_author = normalize_author(entry['author'])
        norm_title = normalize_title(entry['title'])
        year = entry['year']
        key_tuple = (norm_author, norm_title, year)
        new_key = new_map.get(key_tuple)
        if new_key:
            old_to_new[entry['key']] = new_key
        else:
            print(f"Warning: No matching new entry found for original key '{entry['key']}'")
            print(f"  Author: {entry['author']}")
            print(f"  Title: {entry['title']}")
            print(f"  Year: {entry['year']}")
            # Let's also print the normalized version for debugging
            print(f"  Normalized author: {normalize_author(entry['author'])}")
            print(f"  Normalized title: {normalize_title(entry['title'])}")
            print(f"  Year: {entry['year']}")
    
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