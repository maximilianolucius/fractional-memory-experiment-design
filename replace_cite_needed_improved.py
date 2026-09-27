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
        content = f.read()
    
    # Split by '### [' to get each entry block
    blocks = re.split(r'\n### \[', content)
    key_to_entry = {}
    author_year_to_key = {}
    
    for i, block in enumerate(blocks[1:]):  # skip first
        # The block starts with the key and then '] Title\n\n'
        end_key = block.find(']')
        if end_key == -1:
            continue
        key = block[:end_key].strip()
        entry = block[end_key+1:].strip()  # after the ']'
        
        # Extract year: look for (YYYY)
        year_match = re.search(r'\((\d{4})\)', entry)
        if not year_match:
            # Try alternative: . YYYY .
            year_match = re.search(r'\. (\d{4}) \.', entry)
        if not year_match:
            continue
        year = year_match.group(1)
        
        # Extract authors: everything before the year match
        author_part = entry[:year_match.start()].strip()
        # Remove trailing dot if present
        if author_part.endswith('.'):
            author_part = author_part[:-1].strip()
        
        # Extract first author's last name
        # Split by ' and ' to get first author
        first_author = author_part.split(' and ')[0].strip()
        # Check if format is "Last, First"
        if ',' in first_author:
            author_last = first_author.split(',')[0].strip()
        else:
            # Assume last word is last name
            parts = first_author.split()
            author_last = parts[-1] if parts else ''
        
        # Clean: keep only letters, lower case
        author_last = re.sub(r'[^a-zA-Z]', '', author_last).lower()
        
        key_to_entry[key] = (author_last, year, entry)
        author_year_to_key[(author_last, year)] = key
    
    return key_to_entry, author_year_to_key

def extract_author_year_from_old_key(old_key):
    """
    Extract author part and year from an old key like 'sasmal2018' or 'baik2020optimal'.
    Returns (author, year) or (None, None) if not found.
    """
    # Find the first occurrence of four consecutive digits
    year_match = re.search(r'(\d{4})', old_key)
    if not year_match:
        return None, None
    year = year_match.group(1)
    author_part = old_key[:year_match.start()]
    # The author part should be alphabetic; we'll take it as is and lower it.
    author = author_part.lower()
    return author, year

def replace_cite_needed_in_file(filepath, author_year_to_key):
    """
    Replace [[CITE-NEEDED: old_key]] with \cite{new_key} using the mapping.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find [[CITE-NEEDED: ...]]
    pattern = r'\[\{0,2\}\[CITE-NEEDED:\s*([^\]]+)\]\{0,2}\]'
    # Actually, the tags are exactly [[CITE-NEEDED: key]]
    # Let's use a simpler pattern:
    pattern = r'\[\[CITE-NEEDED:\s*([^\]]+)\]\]'
    
    def replace_match(match):
        old_key = match.group(1).strip()
        author, year = extract_author_year_from_old_key(old_key)
        if author is None or year is None:
            # Cannot parse, return original
            return match.group(0)
        # Look up in mapping
        new_key = author_year_to_key.get((author, year))
        if new_key:
            return f'\\cite{{{new_key}}}'
        else:
            # Not found, return original
            return match.group(0)
    
    new_content = re.sub(pattern, replace_match, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    else:
        return False

def main():
    bib_file = '17_BIBLIOGRAPHY.md'
    tex_files = [
        'paper/main.tex',
        'paper/sections/sec8.tex',
        'paper/sections/sec12.tex'
    ]
    
    print(f"Parsing bibliography from {bib_file}...")
    key_to_entry, author_year_to_key = parse_bibliography_md(bib_file)
    print(f"Parsed {len(key_to_entry)} entries.")
    print(f"Author-year mapping has {len(author_year_to_key)} entries.")
    
    # Show a few mappings for verification
    print("\nSample mappings (author, year) -> key:")
    for i, ((author, year), key) in enumerate(list(author_year_to_key.items())[:5]):
        print(f"  ({author}, {year}) -> {key}")
    
    # Process each tex file
    for tex_file in tex_files:
        if not os.path.exists(tex_file):
            print(f"Warning: {tex_file} not found, skipping.")
            continue
        print(f"\nProcessing {tex_file}...")
        changed = replace_cite_needed_in_file(tex_file, author_year_to_key)
        if changed:
            print(f"  Updated {tex_file}")
        else:
            print(f"  No changes made to {tex_file}")
    
    print("\nDone.")

if __name__ == '__main__':
    main()