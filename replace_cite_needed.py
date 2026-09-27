import re
import os

def parse_bibliography_md(filepath):
    """
    Parse the 17_BIBLIOGRAPHY.md file to extract entries.
    Each entry starts with '### [KEY] Author, Year. Title.'
    Returns a dict mapping (author_lastname_lower, year) to key.
    Also returns a dict mapping the raw tag (like 'sasmal2018') to key if we can guess.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by '### [' to get entries
    # The first part is the header, we skip it.
    sections = re.split(r'\n### \[', content)
    # The first element is the preamble, skip it.
    entries = sections[1:] if len(sections) > 1 else []
    
    mapping = {}  # (author_last, year) -> key
    tag_to_key = {}  # for direct tag mapping if we can guess
    
    for entry in entries:
        # Extract the key: it's between '[' and ']'
        key_match = re.match(r'([^\]]+)\]', entry)
        if not key_match:
            continue
        key = key_match.group(1).strip()
        
        # The rest of the entry after the key and the closing bracket
        # We look for the author and year pattern: "Author. (Year)."
        # But note: the author might have multiple names, we take the last name of the first author.
        # Simpler: we look for a year in parentheses.
        year_match = re.search(r'\((\d{4})\)', entry)
        if not year_match:
            continue
        year = year_match.group(1)
        
        # Extract the author part: everything before the year parenthesis.
        # We assume the author is before the year and ends with a dot.
        # Actually, the format is: "Author. (Year). Title."
        # So we can get the substring before the year parenthesis and then extract the last word (author's last name).
        before_year = entry[:year_match.start()]
        # The author string might have multiple parts, we take the last word before the dot.
        # Remove any non-alphanumeric characters and spaces, then take the last word.
        author_part = before_year.strip()
        # Remove the trailing dot if present.
        if author_part.endswith('.'):
            author_part = author_part[:-1]
        # Split by spaces and take the last part as the last name.
        author_parts = author_part.split()
        if author_parts:
            last_name = author_parts[-1].lower()
            # Remove any non-alphabetic characters (like commas, etc.)
            last_name = re.sub(r'[^a-z]', '', last_name)
        else:
            last_name = ''
        
        if last_name and year:
            mapping[(last_name, year)] = key
            # Also create a tag-like key: last_name + year
            tag = f"{last_name}{year}"
            tag_to_key[tag] = key
    
    return mapping, tag_to_key

def find_key_for_tag(tag, mapping, tag_to_key):
    """
    Given a tag like 'sasmal2018', try to find the corresponding key.
    First, try direct match in tag_to_key (which is last_name+year).
    If not, try to split the tag into alphabetic part and numeric part.
    """
    # Direct match
    if tag in tag_to_key:
        return tag_to_key[tag]
    
    # Try to split into letters and digits
    match = re.match(r'([a-zA-Z]+)(\d{4})', tag)
    if match:
        author_part = match.group(1).lower()
        year = match.group(2)
        # Look in mapping by (author_part, year)
        # Note: our mapping uses cleaned last name (only letters)
        cleaned_author = re.sub(r'[^a-z]', '', author_part)
        if (cleaned_author, year) in mapping:
            return mapping[(cleaned_author, year)]
    
    # If not found, return None
    return None

def main():
    # Parse the bibliography
    mapping, tag_to_key = parse_bibliography_md('17_BIBLIOGRAPHY.md')
    print(f"Parsed {len(mapping)} entries from bibliography.")
    print(f"Sample mappings: {list(mapping.items())[:5]}")
    
    # List of CITE-NEEDED tags we found in the paper
    tags = [
        'sasmal2018',
        'gorenflo2020',
        'halanay1966',
        'li2010',
        'baik2020optimal',
        'deng2007parameter',
        'valerio2011fractional'
    ]
    
    # Map each tag to a key
    replacements = {}
    for tag in tags:
        key = find_key_for_tag(tag, mapping, tag_to_key)
        if key:
            replacements[tag] = key
            print(f"Mapped {tag} -> {key}")
        else:
            print(f"WARNING: Could not find key for tag {tag}")
    
    # Now, we need to replace the CITE-NEEDED tags in the paper files.
    # We saw the tags in:
    #   paper/main.tex
    #   paper/sections/sec8.tex
    #   paper/sections/sec12.tex
    # But note: the tags appear in the format:tag]]]]
    # Actually, the pattern we saw was in the format [[CITE-NEEDED: tag]]
    # We need to replace the entire [[CITE-NEEDED: tag]] with the key.
    # However, note that in the file we saw:
    #   [[CITE-NEEDED: sasmal2018]]
    #   [[CITE-NEEDED: gorenflo2020]]
    #   etc.
    #
    # We'll replace each occurrence of [[CITE-NEEDED: tag]] with the key.
    
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
        for tag, key in replacements.items():
            pattern = r'\[\\[CITE-NEEDED: ' + re.escape(tag) + r'\\]\\]'
            replacement = key
            new_content, count = re.subn(pattern, replacement, content)
            if count > 0:
                print(f"Replaced {count} occurrences of {tag} with {key} in {file_path}")
                content = new_content
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print(f"No changes made to {file_path}")

if __name__ == '__main__':
    main()