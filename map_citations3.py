import re

def parse_bib_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    entries = []  # each entry: (key, author_list, year)
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for a line that starts with '### [' (with possible leading spaces)
        stripped = line.lstrip()
        if stripped.startswith('### ['):
            # Extract the key
            match = re.match(r'### \[([A-Z0-9]+)\]', stripped)
            if match:
                key = match.group(1)
                # Now collect the entry lines until next '### [' or end of file
                j = i + 1
                entry_lines = []
                while j < len(lines):
                    next_stripped = lines[j].lstrip()
                    if next_stripped.startswith('### ['):
                        break
                    entry_lines.append(lines[j])
                    j += 1
                entry_text = ' '.join(entry_lines).strip()
                # Extract year: look for parentheses with four digits
                year_match = re.search(r'\((\d{4})\)', entry_text)
                if year_match:
                    year = year_match.group(1)
                    # Extract author part: everything before the year
                    before_year = entry_text[:year_match.start()].strip()
                    # Remove trailing period if any
                    if before_year.endswith('.'):
                        before_year = before_year[:-1]
                    # The author list is before the first comma? Actually the format is:
                    # "Last, F., & ... (year)."
                    # We want the first author's last name (before the first comma)
                    if ',' in before_year:
                        first_author = before_year.split(',')[0].strip()
                    else:
                        # If no comma, maybe the author is the first word? We'll take the first word(s) before a space?
                        # For simplicity, take the first word
                        first_author = before_year.split()[0] if before_year.split() else ''
                    # Clean first_author: remove any trailing punctuation
                    first_author = first_author.rstrip('.')
                    authors = [first_author]  # we only need the first author for mapping
                else:
                    # If no year found, skip this entry
                    i = j
                    continue
                entries.append((key, authors, year))
                i = j
            else:
                i += 1
        else:
            i += 1
    return entries

def main():
    bib_file = '17_BIBLIOGRAPHY.md'
    entries = parse_bib_file(bib_file)
    print(f"Found {len(entries)} entries in bibliography.")
    
    # Build mapping from (author_last_lower, year) to key
    mapping = {}
    for key, authors, year in entries:
        if authors:
            author_last = authors[0].lower()
            mapping[(author_last, year)] = key
    
    # Print some mappings for verification
    print("Sample mappings:")
    for i, ((author, year), key) in enumerate(list(mapping.items())[:10]):
        print(f"  {author} {year} -> {key}")
    
    # Old keys we found in .tex files
    old_keys = ['baik2020optimal', 'chaloner1995bayesian', 'deng2007parameter', 'diethelm2010', 'gorenflo2020', 'halanay1966', 'li2010', 'sasmal2018', 'valerio2011fractional']
    
    # Function to extract author and year from old key
    def extract_from_old_key(key):
        # Find the first occurrence of four consecutive digits
        year_match = re.search(r'(\d{4})', key)
        if not year_match:
            return None, None
        year = year_match.group(1)
        author_part = key[:year_match.start()].rstrip('_')
        return author_part.lower(), year
    
    # Map old keys to new keys
    mapping_old_to_new = {}
    not_found = []
    for old_key in old_keys:
        author, year = extract_from_old_key(old_key)
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
                print(f"  Same author entries: {same_author}")
            not_found.append(old_key)
        else:
            mapping_old_to_new[old_key] = new_key
            print(f"  {old_key} -> {new_key}")
    
    # Write mapping to file
    with open('citation_mapping.txt', 'w') as f:
        for old, new in mapping_old_to_new.items():
            f.write(f"{old} {new}\n")
    print(f"Mapping written to citation_mapping.txt ({len(mapping_old_to_new)} found, {len(not_found)} not found)")
    
    # Also, let's try to find the not_found entries by searching the bibliography text
    if not_found:
        print("\nTrying to find not_found entries in bibliography text...")
        with open(bib_file, 'r', encoding='utf-8') as f:
            bib_text = f.read()
        for old_key in not_found:
            author, year = extract_from_old_key(old_key)
            # Search for author (case insensitive) and year in parentheses
            # We'll look for a pattern: author something (year)
            # Since author might be incomplete, we'll just check if author appears in the text and the year appears in parentheses nearby.
            # We'll do a simple check: if author in bib_text.lower() and f'({year})' in bib_text:
            if author in bib_text.lower() and f'({year})' in bib_text:
                print(f"  Found potential match for {old_key} in bibliography text (author '{author}', year {year})")
            else:
                print(f"  No match for {old_key} in bibliography text")

if __name__ == '__main__':
    main()