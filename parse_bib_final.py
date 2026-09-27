import re
import sys

def parse_bib_file(filename):
    mapping = {}  # (author_last_lower, year) -> key
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for header line
        if line.strip().startswith('### ['):
            # Extract key
            match = re.match(r'### \[([A-Z0-9]+)\]', line.strip())
            if match:
                key = match.group(1)
                # Find the next non-empty line for author info
                j = i + 1
                while j < len(lines) and lines[j].strip() == '':
                    j += 1
                if j >= len(lines):
                    break
                author_line = lines[j].strip()
                # Extract year: look for parentheses with four digits
                year_match = re.search(r'\((\d{4})\)', author_line)
                if year_match:
                    year = year_match.group(1)
                    # Extract author part before the first comma
                    # Author line format: "Last, F., & ... (year)."
                    # We want the part before the first comma
                    if ',' in author_line:
                        author_part = author_line.split(',')[0].strip()
                    else:
                        # If no comma, maybe the author is the first word? We'll take the first word(s) before a space?
                        # For simplicity, take the first word
                        author_part = author_line.split()[0] if author_line.split() else ''
                    # Remove any trailing period
                    author_part = author_part.rstrip('.')
                    # The author part might be like "Caputo, M" but we already split at comma, so author_part is "Caputo"
                    # Convert to lowercase
                    author_last = author_part.lower()
                    mapping[(author_last, year)] = key
                # Move i to j to continue searching from there? Actually we should continue after the header line.
                # We'll set i = j and continue the loop (but we will increment i at the end of loop)
                i = j
            else:
                i += 1
        else:
            i += 1
    return mapping

def extract_author_year_from_old_key(old_key):
    # Find the first occurrence of four consecutive digits
    year_match = re.search(r'(\d{4})', old_key)
    if not year_match:
        return None, None
    year = year_match.group(1)
    author_part = old_key[:year_match.start()].rstrip('_')
    return author_part.lower(), year

def main():
    bib_file = '17_BIBLIOGRAPHY.md'
    mapping = parse_bib_file(bib_file)
    print(f"Parsed {len(mapping)} entries from bibliography.")
    
    # Old keys we found in .tex files
    old_keys = ['baik2020optimal', 'chaloner1995bayesian', 'deng2007parameter', 'diethelm2010', 'gorenflo2020', 'halanay1966', 'li2010', 'sasmal2018', 'valerio2011fractional']
    
    mapping_old_to_new = {}
    not_found = []
    for old_key in old_keys:
        author, year = extract_author_year_from_old_key(old_key)
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
            author, year = extract_author_year_from_old_key(old_key)
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