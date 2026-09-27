import re

def parse_bib_md(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    mapping = {}  # (author_last, year) -> key
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for header line
        header_match = re.match(r'### \[([A-Z0-9]+)\]', line)
        if header_match:
            key = header_match.group(1)
            # Find the next non-empty line that is not a header
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j >= len(lines):
                break
            author_line = lines[j].strip()
            # Extract author part before the first comma
            # Author line format: "Last, F., & ... (YEAR)."
            # We want the part before the first comma
            if ',' in author_line:
                author_part = author_line.split(',')[0].strip()
            else:
                # If no comma, maybe the author is the first word? We'll take first word
                author_part = author_line.split()[0] if author_line.split() else ''
            # Remove any trailing period
            author_part = author_part.rstrip('.')
            # Extract year: look for parentheses with four digits
            year_match = re.search(r'\((\d{4})\)', author_line)
            if year_match:
                year = year_match.group(1)
                author_last = author_part.lower()
                mapping[(author_last, year)] = key
            else:
                # If year not found in author line, we could look in the next lines, but skip for now
                pass
            i = j  # continue after author line? Actually we should continue after the header, but we'll just increment i by 1 and let the loop continue; we might miss some entries but it's okay for now.
        i += 1
    return mapping

def extract_author_year_from_key(key):
    # Find the first occurrence of four consecutive digits
    year_match = re.search(r'(\d{4})', key)
    if not year_match:
        return None, None
    year = year_match.group(1)
    author_part = key[:year_match.start()].rstrip('_')
    # The author part might be the full name or last name; we'll assume it's the last name (lowercase)
    author_last = author_part.lower()
    return author_last, year

def main():
    bib_file = '17_BIBLIOGRAPHY.md'
    mapping = parse_bib_md(bib_file)
    print(f"Parsed {len(mapping)} entries from {bib_file}")
    # Show first few
    for i, ((author, year), key) in enumerate(list(mapping.items())[:5]):
        print(f"  {author} {year} -> {key}")
    
    # Get old keys from .tex files (we can reuse previous extraction)
    # Let's extract them again
    import os
    tex_files = []
    for root, dirs, files in os.walk('paper'):
        for f in files:
            if f.endswith('.tex'):
                tex_files.append(os.path.join(root, f))
    cite_pattern = re.compile(r'\\cite[pt]?\*?\s*\{([^}]+)\}')
    all_keys = set()
    for tf in tex_files:
        with open(tf, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = cite_pattern.findall(content)
            for m in matches:
                for key in m.split(','):
                    key = key.strip()
                    if key:
                        all_keys.add(key)
    print(f"Found {len(all_keys)} unique citation keys in .tex files:")
    print(sorted(all_keys))
    
    mapping_old_to_new = {}
    not_found = []
    for old_key in all_keys:
        author, year = extract_author_year_from_key(old_key)
        if author is None or year is None:
            print(f"Could not extract author/year from {old_key}")
            not_found.append(old_key)
            continue
        new_key = mapping.get((author, year))
        if new_key is None:
            print(f"No mapping found for {old_key} (author={author}, year={year})")
            # Try to find any entry with same author (different year) for hint
            same_author = [k for (a, y), k in mapping.items() if a == author]
            if same_author:
                print(f"Same author entries: {same_author}")
            not_found.append(old_key)
        else:
            mapping_old_to_new[old_key] = new_key
            print(f"  {old_key} -> {new_key}")
    
    # Write mapping to file
    with open('citation_mapping.txt', 'w') as f:
        for old, new in mapping_old_to_new.items():
            f.write(f"{old} {new}\n")
    print(f"Mapping written to citation_mapping.txt ({len(mapping_old_to_new)} found, {len(not_found)} not found)")

if __name__ == '__main__':
    main()