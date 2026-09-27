import re
import os

def parse_bibliography_md(filepath):
    """
    Parse 17_BIBLIOGRAPHY.md
    Returns:
        key_to_entry: dict mapping key -> (author_last, year, full_entry)
        author_year_to_key: dict mapping (author_last, year) -> key
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    entries = []  # each element: (key, content_lines)
    current_key = None
    current_lines = []
    for line in lines:
        if line.startswith('### ['):
            if current_key is not None:
                entries.append((current_key, current_lines))
                current_lines = []
            # extract key: between '[' and ']'
            start = line.find('[') + 1
            end = line.find(']', start)
            current_key = line[start:end]
        else:
            current_lines.append(line)
    if current_key is not None:
        entries.append((current_key, current_lines))
    
    key_to_entry = {}
    author_year_to_key = {}
    
    for key, lines in entries:
        content = ''.join(lines)
        # Try to find author and year
        # Pattern: look for something like "Author. (Year)." or "Author et al. (Year)."
        # We'll look for the first occurrence of a year in parentheses after an author-like string.
        # But we can also look for the pattern: [A-Za-z et al.]+.? \\(\\d{4}\\)
        # However, the author might have commas, etc.
        # Let's try: find all four-digit numbers in parentheses, and assume the one closest to the beginning is the year.
        year_matches = list(re.finditer(r'\\((\\d{4})\\)', content))
        if not year_matches:
            # No year found, skip
            continue
        # Take the first year match
        year_match = year_matches[0]
        year = year_match.group(1)
        # Now we need the author part: everything before the year, but we want the first author's last name.
        # Let's take the substring from the beginning of the content to the year match.
        before_year = content[:year_match.start()]
        # Now we want to extract the first author's last name.
        # The author part might end with a period. Remove trailing spaces and periods.
        before_year = before_year.strip()
        if before_year.endswith('.'):
            before_year = before_year[:-1]
        # Split by non-alphanumeric to get words? Actually, we want the last word of the author part.
        # But the author part might be like "Caputo, M." or "Podlubny, I"
        # We'll split by spaces and non-alphanumeric and take the last alphanumeric word that is not empty.
        words = re.findall(r'[\\w]+', before_year)
        if not words:
            # fallback: use the key's first part? Not ideal.
            author_last = ''
        else:
            # The last word in the author part is likely the last name of the first author.
            # However, if there is a comma, the part before the comma is the last name.
            # Let's check if there is a comma in the before_year string.
            if ',' in before_year:
                # Take the part before the first comma
                author_part = before_year.split(',')[0]
            else:
                # Take the last word
                author_part = words[-1]
            # Clean: remove any non-alphabetic characters (just in case)
            author_last = re.sub(r'[^a-zA-Z]', '', author_part).lower()
        
        if author_last and year:
            key_to_entry[key] = (author_last, year, content)
            author_year_to_key[(author_last, year)] = key
        else:
            # If we couldn't extract author_last, we might still want to map by key? 
            # But for our purpose we need author_last and year.
            pass
    
    return key_to_entry, author_year_to_key

def extract_author_year_from_key(old_key):
    """
    Given a key like 'baik2020optimal', return (author_last, year)
    """
    # Find the first four consecutive digits
    year_match = re.search(r'(\\d{4})', old_key)
    if not year_match:
        return None, None
    year = year_match.group(1)
    author_part = old_key[:year_match.start()]
    # Remove any trailing non-alphabetic characters (like underscores)
    author_part = author_part.rstrip('_')
    # The author part might be the full name or just last name; we'll take the whole thing as last name for simplicity
    # But we need to clean it to only letters and lower case.
    author_last = re.sub(r'[^a-zA-Z]', '', author_part).lower()
    return author_last, year

def main():
    bib_file = '17_BIBLIOGRAPHY.md'
    key_to_entry, author_year_to_key = parse_bibliography_md(bib_file)
    print(f"Parsed {len(key_to_entry)} entries from bibliography.")
    # Print first few for debugging
    for i, (key, (author_last, year, content)) in enumerate(list(key_to_entry.items())[:5]):
        print(f"  {key}: author_last={author_last}, year={year}")
    
    # Old keys we found in the .tex files
    old_keys = ['baik2020optimal', 'chaloner1995bayesian', 'deng2007parameter', 'diethelm2010', 'gorenflo2020', 'halanay1966', 'li2010', 'sasmal2018', 'valerio2011fractional']
    
    mapping_old_to_new = {}
    for old_key in old_keys:
        author_last, year = extract_author_year_from_key(old_key)
        if author_last is None or year is None:
            print(f"Could not extract author/year from {old_key}")
            continue
        new_key = author_year_to_key.get((author_last, year))
        if new_key is None:
            print(f"  For {old_key} ({author_last} {year}): no match found")
            # Debug: show what we have for this author
            possible = [k for (a, y), k in author_year_to_key.items() if a == author_last]
            if possible:
                print(f"    Found entries with author {author_last}: {possible}")
            else:
                print(f"    No entries with author {author_last}")
        else:
            mapping_old_to_new[old_key] = new_key
            print(f"  {old_key} -> {new_key}")
    
    # Now replace in the paper files
    files_to_process = [
        'paper/main.tex',
        'paper/sections/sec8.tex',
        'paper/sections/sec12.tex'
    ]
    
    for file_path in files_to_process:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for old_key, new_key in mapping_old_to_new.items():
            # Pattern: [[CITE-NEEDED: old_key]]
            pattern = r'\\[\\\\[CITE-NEEDED: ' + re.escape(old_key) + r'\\\\]\\\\]'
            replacement = new_key
            new_content, count = re.subn(pattern, replacement, content)
            if count > 0:
                print(f"Replaced {count} occurrences of {old_key} with {new_key} in {file_path}")
                content = new_content
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print(f"No changes made to {file_path}")

if __name__ == '__main__':
    main()