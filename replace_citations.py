import re
import os

def parse_bibtex_file(filepath):
    """Parse a .bib file and return dict: key -> (author_last, year)"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by @article, @book, etc. but we'll assume @article for simplicity
    # Actually, we can split by '@' and then process each entry.
    entries = re.split(r'\n@', content)
    mapping = {}  # key -> (author_last, year)
    for entry in entries[1:]:  # skip first empty part
        entry = entry.strip()
        if not entry:
            continue
        # Extract key: first line until first comma or newline?
        # Actually, the key is after '{' and before the first comma.
        brace_open = entry.find('{')
        if brace_open == -1:
            continue
        after_brace = entry[brace_open+1:]
        comma = after_brace.find(',')
        if comma == -1:
            # maybe no comma? then take until newline?
            newline = after_brace.find('\n')
            if newline == -1:
                key = after_brace.strip()
            else:
                key = after_brace[:newline].strip()
        else:
            key = after_brace[:comma].strip()
        
        # Extract author and year
        author_match = re.search(r'author\s*=\s*{[^}]*}', entry, re.IGNORECASE)
        year_match = re.search(r'year\s*=\s*{[^}]*}', entry, re.IGNORECASE)
        if not author_match or not year_match:
            # try without braces?
            author_match = re.search(r'author\s*=\s*"[^"]*"', entry, re.IGNORECASE)
            year_match = re.search(r'year\s*=\s*"[^"]*"', entry, re.IGNORECASE)
        if author_match and year_match:
            author_str = author_match.group(0)
            # extract content between braces or quotes
            if '{' in author_str:
                author_content = re.search(r'{([^}]*)}', author_str).group(1)
            else:
                author_content = re.search(r'"([^"]*)"', author_str).group(1)
            # Extract first author's last name: assume format "Last, First" or "First Last"
            # We'll take the part before the first comma if exists, else first word?
            # Actually, we want the last name of the first author.
            # If there is 'and', we take the first author before 'and'.
            # For simplicity, we'll take the first word before a comma or space.
            # Remove any braces or quotes already removed.
            # Split by ' and ' to get first author
            first_author = author_content.split(' and ')[0].strip()
            # Now, if there is a comma, the part before comma is last name
            if ',' in first_author:
                author_last = first_author.split(',')[0].strip()
            else:
                # Assume last word is last name? Actually, if format is "First Last", then last word is last name.
                # But could be "First Middle Last". We'll take the last word.
                parts = first_author.split()
                if parts:
                    author_last = parts[-1]
                else:
                    author_last = ''
            # Clean: keep only alphabetic characters
            author_last = re.sub(r'[^a-zA-Z]', '', author_last).lower()
            
            # Year
            if '{' in year_match.group(0):
                year_content = re.search(r'{([^}]*)}', year_match.group(0)).group(1)
            else:
                year_content = re.search(r'"([^"]*)"', year_match.group(0)).group(1)
            year = year_content.strip()
            
            if author_last and year:
                mapping[key] = (author_last, year)
    return mapping

def parse_bibliography_md(filepath):
    """Parse 17_BIBLIOGRAPHY.md and return dict: (author_last, year) -> key"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    entries = []  # each: (key, author_last, year)
    current_key = None
    current_lines = []
    for line in lines:
        if line.startswith('### ['):
            if current_key is not None:
                # process previous entry
                content = ''.join(current_lines)
                # extract author_last and year from content
                author_last, year = extract_author_year_from_content(content)
                if author_last and year:
                    entries.append((current_key, author_last, year))
                current_lines = []
            # extract key
            start = line.find('[') + 1
            end = line.find(']', start)
            current_key = line[start:end]
        else:
            current_lines.append(line)
    if current_key is not None:
        content = ''.join(current_lines)
        author_last, year = extract_author_year_from_content(content)
        if author_last and year:
            entries.append((current_key, author_last, year))
    
    mapping = {}  # (author_last, year) -> key
    for key, author_last, year in entries:
        # If duplicate, we keep the first? but should be unique.
        if (author_last, year) not in mapping:
            mapping[(author_last, year)] = key
    return mapping

def extract_author_year_from_content(content):
    """Extract author_last and year from a bibliography entry in 17_BIBLIOGRAPHY.md"""
    # Look for year in parentheses
    year_match = re.search(r'\\((\\d{4})\\)', content)
    if not year_match:
        return None, None
    year = year_match.group(1)
    # Get the part before the year
    before_year = content[:year_match.start()]
    # Find the last word before the year that is likely the author's last name
    # Remove trailing punctuation and spaces
    before_year = before_year.strip()
    if before_year.endswith('.'):
        before_year = before_year[:-1]
    # Split into words (alphanumeric sequences)
    words = re.findall(r'[\\w]+', before_year)
    if not words:
        return None, year
    # The last word is likely the last name of the first author
    # However, if there is a comma, the part before comma is the last name.
    # Let's reconstruct the string before year and look for a comma.
    if ',' in before_year:
        # Take the part before the first comma
        author_part = before_year.split(',')[0]
    else:
        # Take the last word
        author_part = words[-1]
    # Clean: keep only alphabetic
    author_last = re.sub(r'[^a-zA-Z]', '', author_part).lower()
    return author_last, year

def extract_author_year_from_tag(tag):
    """Extract author_last and year from a tag like 'sasmal2018'"""
    match = re.match(r'([a-zA-Z]+)(\\d{4})', tag)
    if match:
        author_part = match.group(1).lower()
        # keep only alphabetic
        author_last = re.sub(r'[^a-z]', '', author_part)
        year = match.group(2)
        return author_last, year
    return None, None

def main():
    # Step 1: Parse the old bibliography (submission/bibliography.bib) to get old_key -> (author_last, year)
    old_bib = parse_bibtex_file('submission/bibliography.bib')
    print(f"Parsed {len(old_bib)} entries from old bibliography.")
    # Print a few for verification
    for i, (key, (author, year)) in enumerate(list(old_bib.items())[:5]):
        print(f"  {key}: {author} {year}")
    
    # Step 2: Parse 17_BIBLIOGRAPHY.md to get (author_last, year) -> new_key
    new_map = parse_bibliography_md('17_BIBLIOGRAPHY.md')
    print(f"Parsed {len(new_map)} entries from 17_BIBLIOGRAPHY.md.")
    for i, ((author, year), key) in enumerate(list(new_map.items())[:5]):
        print(f"  {author} {year}: {key}")
    
    # Step 3: Build mapping from old_key to new_key
    old_to_new = {}
    for old_key, (author_last, year) in old_bib.items():
        new_key = new_map.get((author_last, year))
        if new_key:
            old_to_new[old_key] = new_key
        else:
            print(f"WARNING: No match for old key '{old_key}' (author: {author_last}, year: {year})")
    
    print(f"Created mapping for {len(old_to_new)} old keys to new keys.")
    
    # Step 4: Replace CITE-NEEDED tags in .tex files
    # The tags we need to replace are the old keys that appear as [[CITE-NEEDED: old_key]]
    # We have the mapping old_to_new.
    tex_files = []
    for root, dirs, files in os.walk('paper'):
        for file in files:
            if file.endswith('.tex'):
                tex_files.append(os.path.join(root, file))
    # Also check manuscript/sections if exists
    if os.path.exists('manuscript/sections'):
        for root, dirs, files in os.walk('manuscript/sections'):
            for file in files:
                if file.endswith('.tex'):
                    tex_files.append(os.path.join(root, file))
    
    for tex_file in tex_files:
        if not os.path.exists(tex_file):
            continue
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for old_key, new_key in old_to_new.items():
            # Pattern: [[CITE-NEEDED: old_key]]
            pattern = r'\\[\\\\[CITE-NEEDED: ' + re.escape(old_key) + r'\\\\]\\\\]'
            replacement = new_key
            new_content, count = re.subn(pattern, replacement, content)
            if count > 0:
                print(f"Replaced {count} occurrences of {old_key} with {new_key} in {tex_file}")
                content = new_content
        
        if content != original_content:
            with open(tex_file, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            # No changes, but we still might want to check if there are any CITE-NEEDED left?
            pass

if __name__ == '__main__':
    main()