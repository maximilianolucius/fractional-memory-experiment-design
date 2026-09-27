import re
import os

def parse_bibliography(filename):
    """Parse the bibliography markdown file.
    Returns a list of tuples: (key, author_list, year)
    where author_list is a list of author strings (as given before the year).
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by lines
    lines = content.split('\n')
    entries = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for a line that starts with '### ['
        if line.strip().startswith('### ['):
            # Extract the key
            match = re.match(r'### \[([A-Z0-9]+)\]', line.strip())
            if match:
                key = match.group(1)
                # Now collect the entry lines until next '### [' or end of file
                j = i + 1
                entry_lines = []
                while j < len(lines) and not lines[j].strip().startswith('### ['):
                    entry_lines.append(lines[j])
                    j += 1
                entry_text = ' '.join(entry_lines).strip()
                # Extract author and year: look for pattern 'Author..., (year)'
                # We'll find the first author (before first comma) and the year in parentheses
                # Find the year pattern
                year_match = re.search(r'\((\d{4})\)', entry_text)
                if year_match:
                    year = year_match.group(1)
                    # Get the part before the year
                    before_year = entry_text[:year_match.start()].strip()
                    # Remove any trailing period
                    if before_year.endswith('.'):
                        before_year = before_year[:-1]
                    # The author part is before the first comma? Actually the author list may have 'and' or '&'
                    # We'll take the first author: split by ',' and take first part
                    if ',' in before_year:
                        first_author = before_year.split(',')[0].strip()
                    else:
                        # If no comma, maybe the author is the first word? We'll take the first word(s) before a space?
                        # For simplicity, take the first word
                        first_author = before_year.split()[0] if before_year.split() else ''
                    # Clean first_author: remove any trailing punctuation
                    first_author = first_author.rstrip('.')
                    authors = [first_author]  # we only need first author for mapping
                else:
                    # If no year found, skip
                    i = j
                    continue
                entries.append((key, authors, year))
                i = j
            else:
                i += 1
        else:
            i += 1
    return entries

def build_mapping(entries):
    """Build mapping from (author_last_lower, year) to key."""
    mapping = {}
    for key, authors, year in entries:
        if authors:
            author_last = authors[0].lower()
            # Remove any non-alphabetic characters? Keep as is.
            mapping[(author_last, year)] = key
    return mapping

def extract_author_year_from_old_key(old_key):
    """Extract author part and year from old key like 'baik2020optimal'.
    Returns (author_part, year) where author_part is the string before the year (lowered, stripped of underscores).
    """
    year_match = re.search(r'(\d{4})', old_key)
    if not year_match:
        return None, None
    year = year_match.group(1)
    author_part = old_key[:year_match.start()].rstrip('_')
    return author_part.lower(), year

def main():
    bib_file = '17_BIBLIOGRAPHY.md'
    entries = parse_bibliography(bib_file)
    print(f"Parsed {len(entries)} entries from bibliography.")
    # Show first few
    for key, authors, year in entries[:5]:
        print(f"  {key}: {authors} ({year})")
    
    mapping = build_mapping(entries)
    print(f"Built mapping with {len(mapping)} entries.")
    
    # Find all citation keys in .tex files
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
    
    # Map old keys to new keys
    mapping_old_to_new = {}
    not_found = []
    for old_key in all_keys:
        author_part, year = extract_author_year_from_old_key(old_key)
        if author_part is None or year is None:
            print(f"Could not extract author/year from {old_key}")
            not_found.append(old_key)
            continue
        new_key = mapping.get((author_part, year))
        if new_key is None:
            print(f"No mapping found for {old_key} (author='{author_part}', year={year})")
            # Try to find any entry with same author (different year) for hint
            same_author = [k for (a, y), k in mapping.items() if a == author_part]
            if same_author:
                print(f  Same author entries: {same_author}")
            not_found.append(old_key)
        else:
            mapping_old_to_new[old_key] = new_key
            print(f"  {old_key} -> {new_key}")
    
    # Write mapping to file
    with open('citation_mapping.txt', 'w') as f:
        for old, new in mapping_old_to_new.items():
            f.write(f"{old} {new}\n")
    print(f"Mapping written to citation_mapping.txt ({len(mapping_old_to_new)} found, {len(not_found)} not found)")
    
    # Additionally, let's try to find the not_found entries by searching the bibliography text
    if not_found:
        print("\nTrying to find not_found entries in bibliography text...")
        with open(bib_file, 'r', encoding='utf-8') as f:
            bib_text = f.read()
        for old_key in not_found:
            author_part, year = extract_author_year_from_old_key(old_key)
            # Search for author_part (case insensitive) and year in parentheses
            # We'll look for a pattern: author_part something (year)
            # Since author_part might be incomplete, we'll just see if the author_part appears in the text near the year.
            # We'll do a simple search: if author_part in bib_text.lower() and f'({year})' in bib_text:
            if author_part in bib_text.lower() and f'({year})' in bib_text:
                print(f"  Found potential match for {old_key} in bibliography text (author '{author_part}', year {year})")
            else:
                print(f"  No match for {old_key} in bibliography text")

if __name__ == '__main__':
    main()