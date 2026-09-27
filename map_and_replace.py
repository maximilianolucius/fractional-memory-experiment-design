import re
import os

def parse_bibliography_md(filepath):
    """
    Parse 17_BIBLIOGRAPHY.md
    Returns dict: key -> (author_last, year, full_entry)
    Also returns dict: (author_last, year) -> key
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by '\n### [' to get entries
    sections = re.split(r'\n### \\[', content)
    # First section is preamble
    entries = sections[1:] if len(sections) > 1 else []
    
    key_to_info = {}  # key -> (author_last, year, entry_text)
    author_year_to_key = {}  # (author_last, year) -> key
    
    for entry in entries:
        # Extract key: between [ and ]
        key_match = re.match(r'([^\\]]+)\\]', entry)
        if not key_match:
            continue
        key = key_match.group(1).strip()
        
        # The rest of the entry after the key and closing bracket
        # We'll look for the author and year in the first few lines
        # Find the first line that contains a year in parentheses
        lines = entry.split('\n')
        author_line = None
        year = None
        for line in lines:
            # Look for pattern like "Author. (Year)."
            year_match = re.search(r'\\((\\d{4})\\)', line)
            if year_match:
                year = year_match.group(1)
                # Author part is before the year parenthesis
                author_part = line[:year_match.start()].strip()
                # Remove trailing dot if present
                if author_part.endswith('.'):
                    author_part = author_part[:-1]
                # Assume the last word is the last name of the first author
                # Remove any non-alphabetic characters from the end
                author_part = re.sub(r'[^\\w\\s]', '', author_part)
                author_parts = author_part.split()
                if author_parts:
                    author_last = author_parts[-1].lower()
                else:
                    author_last = ''
                author_line = line
                break
        if author_last and year:
            key_to_info[key] = (author_last, year, entry)
            author_year_to_key[(author_last, year)] = key
        # If we didn't find a year, skip? but we expect all entries to have year
    
    return key_to_info, author_year_to_key

def extract_author_year_from_tag(tag):
    """
    Extract author part (lowercase, alphabetic only) and year from a tag like 'sasmal2018'
    Returns (author_last, year) or (None, None)
    """
    match = re.match(r'([a-zA-Z]+)(\\d{4})', tag)
    if match:
        author_part = match.group(1).lower()
        # Keep only alphabetic characters
        author_last = re.sub(r'[^a-z]', '', author_part)
        year = match.group(2)
        return author_last, year
    return None, None

def main():
    bib_file = '17_BIBLIOGRAPHY.md'
    key_to_info, author_year_to_key = parse_bibliography_md(bib_file)
    print(f"Parsed {len(key_to_info)} entries from bibliography.")
    
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
    
    replacements = {}  # tag -> new_key
    for tag in tags:
        author_last, year = extract_author_year_from_tag(tag)
        if author_last is None or year is None:
            print(f"WARNING: Could not parse tag {tag}")
            continue
        key = author_year_to_key.get((author_last, year))
        if key:
            replacements[tag] = key
            print(f"Mapped {tag} -> {key}")
        else:
            print(f"WARNING: No matching entry for author_last='{author_last}', year='{year}'")
            # Debug: show what we have for this author
            possible = [k for (a, y), k in author_year_to_key.items() if a == author_last]
            if possible:
                print(f"  Found entries with author {author_last}: {possible}")
            else:
                print(f"  No entries with author {author_last}")
    
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
        for tag, key in replacements.items():
            # Pattern: [[CITE-NEEDED: tag]]
            pattern = r'\\[\\\\[CITE-NEEDED: ' + re.escape(tag) + r'\\\\]\\\\]'
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