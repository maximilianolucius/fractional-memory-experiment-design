import re
import subprocess
import sys
import os

def parse_bibtex_simple(content):
    """Parse BibTeX content, returning list of dicts with key, author, title, year."""
    entries = []
    # Split by '@' and process each block
    blocks = re.split(r'\n@', content)
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # Find the opening brace after the type
        # Pattern: @type{key,
        brace_open = block.find('{')
        if brace_open == -1:
            continue
        # Extract the key: everything from after the '{' until the first comma
        after_brace = block[brace_open+1:]
        comma = after_brace.find(',')
        if comma == -1:
            continue
        key = after_brace[:comma].strip()
        # Now we need to extract the fields. We'll look for the whole entry until the matching '}'
        # We'll find the matching brace for the outer braces.
        brace_count = 0
        in_brace = False
        end_idx = -1
        for i, ch in enumerate(block):
            if ch == '{':
                if not in_brace:
                    in_brace = True
                brace_count += 1
            elif ch == '}':
                brace_count -= 1
                if brace_count == 0 and in_brace:
                    end_idx = i
                    break
        if end_idx == -1:
            # Fallback: take the rest of the block
            field_str = block[brace_open+1:]
        else:
            field_str = block[brace_open+1:end_idx]
        # Now parse fields: look for patterns like author = { ... }, title = { ... }, etc.
        fields = {}
        # We'll use a regex to match each field: (\w+)\s*=\s*{([^}]*)}
        # This assumes no nested braces.
        field_pattern = re.compile(r'(\w+)\s*=\s*{([^}]*)}')
        for match in field_pattern.finditer(field_str):
            field_name = match.group(1).lower()
            field_value = match.group(2).strip()
            fields[field_name] = field_value
        # We only need author, title, year for matching
        entry = {
            'key': key,
            'author': fields.get('author', ''),
            'title': fields.get('title', ''),
            'year': fields.get('year', '')
        }
        entries.append(entry)
    return entries

def normalize_author(author):
    author = author.lower()
    author = re.sub(r'\s+', ' ', author)
    return author.strip()

def normalize_title(title):
    title = title.lower()
    title = re.sub(r'\s+', ' ', title)
    return title.strip()

def main():
    # Get original bibliography from git
    try:
        original_bib_content = subprocess.check_output(
            ['git', 'show', 'HEAD:paper/bibliography.bib'],
            stderr=subprocess.DEVNULL,
            text=True
        )
    except subprocess.CalledProcessError:
        print("Could not retrieve original bibliography from git")
        sys.exit(1)
    
    # Read current bibliography
    with open('paper/bibliography.bib', 'r', encoding='utf-8') as f:
        current_bib_content = f.read()
    
    original_entries = parse_bibtex_simple(original_bib_content)
    current_entries = parse_bibtex_simple(current_bib_content)
    
    print(f"Original entries: {len(original_entries)}")
    for e in original_entries:
        print(f"  {e['key']}: {e['author']} - {e['title']} - {e['year']}")
    print(f"Current entries: {len(current_entries)}")
    for e in current_entries[:5]:  # print first 5
        print(f"  {e['key']}: {e['author']} - {e['title']} - {e['year']}")
    if len(current_entries) > 5:
        print("  ...")
    
    # Build mapping from (author, title, year) to current key
    current_map = {}
    for e in current_entries:
        key = (normalize_author(e['author']), normalize_title(e['title']), e['year'])
        if key not in current_map:
            current_map[key] = e['key']
        else:
            print(f"Warning: duplicate signature {key}")
    
    # Map original keys to current keys
    old_to_new = {}
    for e in original_entries:
        key = (normalize_author(e['author']), normalize_title(e['title']), e['year'])
        new_key = current_map.get(key)
        if new_key:
            old_to_new[e['key']] = new_key
        else:
            print(f"Warning: No matching current entry for original key '{e['key']}'")
            print(f"  Author: {e['author']}")
            print(f"  Title: {e['title']}")
            print(f"  Year: {e['year']}")
    
    print(f"Created mapping for {len(old_to_new)} original keys to current keys.")
    if old_to_new:
        print("Mapping:", old_to_new)
    
    # Update citation keys in .tex files
    for root, dirs, files in os.walk('paper'):
        for file in files:
            if file.endswith('.tex'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Replace each old key with new key
                for old_key, new_key in old_to_new.items():
                    # Use word boundaries to avoid partial matches
                    pattern = r'\b' + re.escape(old_key) + r'\b'
                    content = re.sub(pattern, new_key, content)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
    print("Updated citation keys in .tex files.")
    
    # Run bibtex and pdflatex to verify
    print("Running bibtex...")
    result_bibtex = subprocess.run(['bibtex', 'paper/main'], capture_output=True, text=True)
    print(f"BibTeX exit code: {result_bibtex.returncode}")
    if result_bibtex.returncode != 0:
        print("BibTeX stderr:")
        print(result_bibtex.stderr[-500:])
    print("Running pdflatex...")
    result_pdflatex = subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', '-output-directory=paper', 'paper/main.tex'],
        capture_output=True, text=True
    )
    print(f"Pdflatex exit code: {result_pdflatex.returncode}")
    if result_pdflatex.returncode != 0:
        print("Pdflatex stderr:")
        print(result_pdflatex.stderr[-500:])
    else:
        print("LaTeX compilation succeeded.")
    
    # Final count of entries in bibliography.bib
    with open('paper/bibliography.bib', 'r', encoding='utf-8') as f:
        bib_content = f.read()
    num_entries = len(re.findall(r'@\\w+{', bib_content))
    print(f"Number of entries in bibliography.bib: {num_entries}")

if __name__ == '__main__':
    main()