import re
import sys

def parse_bib_md(filename):
    """Parse 17_BIBLIOGRAPHY.md and return a dict mapping (author_last, year) to key."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by '### [' to get each entry
    entries = re.split(r'\n### \[', content)
    # First element is the header, skip
    mapping = {}
    for entry in entries[1:]:
        # Extract key: everything between [ and ] until the first ] after the opening [
        match = re.match(r'([^\]]+)\]\s*(.*)', entry, re.DOTALL)
        if not match:
            continue
        key = match.group(1).strip()
        rest = match.group(2)
        
        # Extract author: first line after the header, until the first period or newline?
        # Actually, the format is:
        # ### [F01]
        # Caputo, M. (1967). Linear models of dissipation whose Q is almost frequency independent—II. *Geophysical Journal International*, **13**(5), 529–539. DOI: `10.1111/j.1365-246X.1967.tb02303.x`
        #
        # So we can get the first line after the header (which is the author line)
        lines = rest.strip().split('\n')
        if not lines:
            continue
        author_line = lines[0].strip()
        # Extract year: look for a four-digit number in parentheses after the author
        year_match = re.search(r'\((\d{4})\)', author_line)
        if not year_match:
            # Sometimes the year is in the next line? Let's look at the first two lines combined
            first_two = ' '.join(lines[:2])
            year_match = re.search(r'\((\d{4})\)', first_two)
        if year_match:
            year = year_match.group(1)
            # Extract author name: everything before the year parentheses
            author_part = author_line.split('(')[0].strip()
            # Remove trailing period if any
            if author_part.endswith('.'):
                author_part = author_part[:-1]
            # Take the first author's last name (everything before the first comma)
            # If there's a comma, take the part before the comma
            if ',' in author_part:
                author_last = author_part.split(',')[0].strip()
            else:
                # If no comma, assume the first word is the last name? Not ideal but fallback
                author_last = author_part.split()[0].strip()
            # Clean up author_last: remove any trailing punctuation
            author_last = author_last.rstrip('.')
            key_author_year = (author_last.lower(), year)
            # If there are multiple entries with same author_last and year, we'll keep the first for now
            if key_author_year not in mapping:
                mapping[key_author_year] = key
            else:
                # If duplicate, we could try to disambiguate by title, but for now skip
                pass
    return mapping

def extract_author_year_from_key(old_key):
    """Extract author last name and year from a key like 'baik2020optimal'."""
    # Find the first four consecutive digits
    year_match = re.search(r'(\d{4})', old_key)
    if not year_match:
        return None, None
    year = year_match.group(1)
    # Everything before the year is the author part
    author_part = old_key[:year_match.start()]
    # Remove any trailing non-alphabetic characters (like underscores)
    author_part = author_part.rstrip('_')
    # The author part might be the full name or just last name; we'll take the whole thing as last name for simplicity
    # Convert to lowercase for comparison
    author_last = author_part.lower()
    return author_last, year

def main():
    bib_file = '17_BIBLIOGRAPHY.md'
    mapping = parse_bib_md(bib_file)
    print(f"Parsed {len(mapping)} author-year -> key mappings from {bib_file}")
    # Print first few for debugging
    for i, ((author, year), key) in enumerate(list(mapping.items())[:5]):
        print(f"  {author} {year} -> {key}")
    
    # Old keys we found in the .tex files
    old_keys = ['baik2020optimal', 'chaloner1995bayesian', 'deng2007parameter', 'diethelm2010', 'gorenflo2020', 'halanay1966', 'li2010', 'sasmal2018', 'valerio2011fractional']
    
    mapping_old_to_new = {}
    for old_key in old_keys:
        author, year = extract_author_year_from_key(old_key)
        if author is None or year is None:
            print(f"Could not extract author/year from {old_key}")
            continue
        key = mapping.get((author, year))
        if key is None:
            # Try to find any key with the same author (ignoring year) for debugging
            possible = [k for (a, y), k in mapping.items() if a == author]
            if possible:
                print(f"  For {old_key} ({author} {year}): found multiple years: {possible}")
            else:
                print(f"  For {old_key} ({author} {year}): no match found")
        else:
            mapping_old_to_new[old_key] = key
            print(f"  {old_key} -> {key}")
    
    # Write mapping to a file for use in replacement
    with open('citation_mapping.txt', 'w') as f:
        for old, new in mapping_old_to_new.items():
            f.write(f"{old} {new}\n")
    
    return mapping_old_to_new

if __name__ == '__main__':
    main()