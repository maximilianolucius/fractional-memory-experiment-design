import re

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
    # Each block starts with '### [KEY] Title'
    blocks = re.split(r'\n### \[', content)
    # The first block is the header before any ### [
    # We'll process blocks[1:] but note that the split removed the '### [' so we need to add it back for the key extraction?
    # Actually, each block after the first starts with the KEY] Title ...
    key_to_entry = {}
    author_year_to_key = {}
    
    for i, block in enumerate(blocks[1:]):  # skip first
        # The block starts with the key and then '] Title\n\n'
        # Find the closing bracket of the key
        end_key = block.find(']')
        if end_key == -1:
            continue
        key = block[:end_key].strip()
        # The rest of the block is the entry
        entry = block[end_key+1:].strip()  # after the ']'
        # Now we need to extract author and year from the entry
        # The entry format: Authors. (Year). Title. Journal, Volume(Issue), pages. DOI: `doi`
        # We'll look for a pattern: (.*) \(\d{4}\.
        # But author list can have multiple authors.
        # We'll extract the year first: look for a four-digit number in parentheses after the authors.
        year_match = re.search(r'\((\d{4})\)', entry)
        if not year_match:
            # Try without parentheses? Sometimes year is in brackets?
            year_match = re.search(r'\. (\d{4}) \.', entry)
        if year_match:
            year = year_match.group(1)
        else:
            # If we can't find year, skip
            continue
        
        # Extract authors: everything before the year parentheses
        # We'll take the string up to the year match
        author_part = entry[:year_match.start()].strip()
        # Remove trailing dot if any
        if author_part.endswith('.'):
            author_part = author_part[:-1].strip()
        # Now extract the first author's last name
        # Authors are separated by ' and ' or ','
        # We'll split by ' and ' first, then take the first part
        first_author = author_part.split(' and ')[0].strip()
        # Now, the first author might be in format "Last, First" or "First Last"
        if ',' in first_author:
            # Format: "Last, First"
            author_last = first_author.split(',')[0].strip()
        else:
            # Assume last word is last name
            parts = first_author.split()
            if parts:
                author_last = parts[-1]
            else:
                author_last = ''
        # Clean author_last: keep only letters
        author_last = re.sub(r'[^a-zA-Z]', '', author_last).lower()
        
        # Store
        key_to_entry[key] = (author_last, year, entry)
        author_year_to_key[(author_last, year)] = key
    
    return key_to_entry, author_year_to_key

if __name__ == '__main__':
    key_to_entry, author_year_to_key = parse_bibliography_md('17_BIBLIOGRAPHY.md')
    print(f"Parsed {len(key_to_entry)} entries.")
    # Print a few for debugging
    for i, (key, (author, year, entry)) in enumerate(list(key_to_entry.items())[:5]):
        print(f"{key}: {author} {year}")
        # Print first 100 chars of entry
        print(entry[:100])
        print()