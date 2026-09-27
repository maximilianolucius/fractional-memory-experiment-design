import re
import subprocess
import sys
import os

def normalize_author(author):
    """Normalize author string for comparison."""
    author = author.lower()
    author = re.sub(r'\s+', ' ', author)
    return author.strip()

def normalize_title(title):
    """Normalize title string for comparison."""
    title = title.lower()
    title = re.sub(r'\s+', ' ', title)
    return title.strip()

def parse_bibtex(content):
    """
    Parse a BibTeX string into a list of entries.
    Each entry is a dict with keys: 'key', 'fields' (dict of field names to values).
    We only need key, author, title, year for matching.
    """
    entries = []
    # Split by '@' and process each block
    blocks = re.split(r'\n@', content)
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # Find the first '{' that starts the entry fields
        # The pattern is: @type{key,
        # We want to extract the type and key, but we don't need the type for matching.
        # We'll look for the pattern: {key,
        match = re.search(r'\{\s*([^,]+)\s*,', block)
        if not match:
            continue
        key = match.group(1).strip()
        # Now, we want to extract the fields. We'll look for the field patterns.
        # We'll take the part after the opening brace until the closing brace at the same level.
        # Since we don't have nested braces in values, we can simply find the matching brace.
        # But let's do a simple approach: extract everything between the first '{' and the last '}'
        # that is at the same indentation? We'll assume the entry ends with a '}' that is not inside a field value.
        # We'll find the index of the first '{'
        start_brace = block.find('{')
        # Now we need to find the matching '}'. We'll count braces.
        brace_count = 0
        end_brace = -1
        for i, ch in enumerate(block[start_brace:], start_brace):
            if ch == '{':
                brace_count += 1
            elif ch == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_brace = i
                    break
        if end_brace == -1:
            # If we didn't find a matching brace, skip.
            continue
        field_str = block[start_brace+1:end_brace].strip()
        # Now parse the field string: each line is a field
        fields = {}
        # Split by newline and process each line
        for line in field_str.split('\\n'):
            line = line.strip()
            if not line:
                continue
            # Remove trailing comma if present
            if line.endswith(','):
                line = line[:-1].strip()
            # Now line should be: key = { value }
            if '=' not in line:
                continue
            key_part, value_part = line.split('=', 1)
            key_part = key_part.strip()
            value_part = value_part.strip()
            # Value should be enclosed in {...}
            if value_part.startswith('{') and value_part.endswith('}'):
                value = value_part[1:-1].strip()
            else:
                # Maybe it's quoted? We'll skip for now.
                continue
            fields[key_part.lower()] = value  # Store field names in lowercase for consistency
        entries.append({
            'key': key,
            'fields': fields
        })
    return entries

def main():
    # Get original bibliography from git
    try:
        original_bib_content = subprocess.check_output(
            ['git', 'show', 'HEAD:paper/bibliography.bib'],
            stderr=subprocess.DEVNULL,
            text=True
        )
    except subprocess.CalledProcessError:
        print("Could not retrieve original bibliography from git. Proceeding without key replacement.")
        original_bib_content = ""
    
    # Read current bibliography
    with open('paper/bibliography.bib', 'r', encoding='utf-8') as f:
        current_bib_content = f.read()
    
    # Parse both
    original_entries = parse_bibtex(original_bib_content) if original_bib_content else []
    current_entries = parse_bibtex(current_bib_content)
    
    print(f"Parsed {len(original_entries)} original bibliography entries.")
    print(f"Parsed {len(current_entries)} current bibliography entries.")
    
    # Build mapping from (author, title, year) to current key for current entries
    current_map = {}
    for entry in current_entries:
        fields = entry['fields']
        author = fields.get('author', '')
        title = fields.get('title', '')
        year = fields.get('year', '')
        key = entry['key']
        norm_author = normalize_author(author)
        norm_title = normalize_title(title)
        signature = (norm_author, norm_title, year)
        # If there's already an entry for this signature, we keep the first? But there shouldn't be duplicates.
        if signature not in current_map:
            current_map[signature] = key
        else:
            print(f"Warning: duplicate signature in current bibliography: {signature}")
    
    # Map original keys to current keys
    old_to_new = {}
    for entry in original_entries:
        fields = entry['fields']
        author = fields.get('author', '')
        title = fields.get('title', '')
        year = fields.get('year', '')
        key = entry['key']
        norm_author = normalize_author(author)
        norm_title = normalize_title(title)
        signature = (norm_author, norm_title, year)
        new_key = current_map.get(signature)
        if new_key:
            old_to_new[key] = new_key
        else:
            print(f"Warning: No matching current entry for original key '{key}'")
            print(f"  Author: {author}")
            print(f"  Title: {title}")
            print(f"  Year: {year}")
    
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