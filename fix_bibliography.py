import re
import os
import subprocess

def normalize_author(author):
    author = author.lower()
    author = re.sub(r'\s+', ' ', author)
    return author.strip()

def normalize_title(title):
    title = title.lower()
    title = re.sub(r'\s+', ' ', title)
    return title.strip()

def parse_citation_line(line):
    # Parse a line like:
    # "Caputo, M. (1967). Linear models of dissipation whose Q is almost frequency independent—II. *Geophysical Journal International*, **13**(5), 529–539. DOI: `10.1111/j.1365-246X.1967.tb02303.x`."
    # Returns a dict with keys: author, year, title, journal, volume, number, pages, doi
    # If a field is not found, it will be empty string.
    
    # Split by '. ' to get parts
    parts = line.split('. ')
    if len(parts) < 3:
        return None
    
    author_part = parts[0].strip()
    year_part = parts[1].strip() if len(parts) > 1 else ''
    title_part = parts[2].strip() if len(parts) > 2 else ''
    rest = '. '.join(parts[3:]) if len(parts) > 3 else ''
    
    # Extract year from year_part: look for (yyyy)
    year_match = re.search(r'\((\d{4})\)', year_part)
    if year_match:
        year = year_match.group(1)
    else:
        # Try to find any four-digit number
        year_match = re.search(r'(\d{4})', year_part)
        year = year_match.group(1) if year_match else ''
    
    # Now parse the rest for journal, volume, number, pages, doi
    journal = ''
    volume = ''
    number = ''
    pages = ''
    doi = ''
    
    # Look for journal: *...*
    journal_match = re.search(r'\*([^*]+)\*', rest)
    if journal_match:
        journal = journal_match.group(1)
        # Remove this occurrence from rest to avoid double counting
        rest = rest.replace(journal_match.group(0), '', 1)
    
    # Look for volume and number: **vol**(num)
    vol_issue_match = re.search(r'\*\*(\d+)\*\*\((\d+)\)', rest)
    if vol_issue_match:
        volume = vol_issue_match.group(1)
        number = vol_issue_match.group(2)
        rest = rest.replace(vol_issue_match.group(0), '', 1)
    else:
        # Look for just volume: **vol**
        vol_match = re.search(r'\*\*(\d+)\*\*', rest)
        if vol_match:
            volume = vol_match.group(1)
            rest = rest.replace(vol_match.group(0), '', 1)
    
    # Look for pages: digits-separated-by-en-dash or hyphen, possibly with spaces
    pages_match = re.search(r'(\d+[\s\u2013-]\d+)', rest)  # \u2013 is en dash
    if pages_match:
        pages = pages_match.group(1).strip()
        rest = rest.replace(pages_match.group(0), '', 1)
    
    # Look for DOI: `...`
    doi_match = re.search(r'`([^`]+)`', rest)
    if doi_match:
        doi = doi_match.group(1)
        rest = rest.replace(doi_match.group(0), '', 1)
    
    # Clean up extra spaces and dots from the fields
    author_part = author_part.strip()
    title_part = title_part.strip()
    journal = journal.strip()
    volume = volume.strip()
    number = number.strip()
    pages = pages.strip()
    doi = doi.strip()
    
    return {
        'author': author_part,
        'year': year,
        'title': title_part,
        'journal': journal,
        'volume': volume,
        'number': number,
        'pages': pages,
        'doi': doi
    }

def parse_bibtex(content):
    """Parse BibTeX content and return a list of dicts with key and fields."""
    entries = []
    # Pattern to match @type{key, ...} 
    # We'll use a simple approach: split by '@' and then parse each.
    parts = content.split('@')
    for part in parts[1:]:
        brace_open = part.find('{')
        if brace_open == -1:
            continue
        typ = part[:brace_open].strip()
        after_brace = part[brace_open+1:]
        # Find the key: everything until the first comma
        comma = after_brace.find(',')
        if comma == -1:
            continue
        key = after_brace[:comma].strip()
        field_str = after_brace[comma+1:]  # everything after the comma
        # Parse fields: look for \w+ = { ... }
        field_pattern = re.compile(r'(\w+)\s*=\s*\{([^}]*)\}')
        fields = {}
        for match in field_pattern.finditer(field_str):
            field_name = match.group(1).lower()
            field_value = match.group(2).strip()
            fields[field_name] = field_value
        entries.append({
            'type': typ,
            'key': key,
            'fields': fields
        })
    return entries

def main():
    md_path = '17_BIBLIOGRAPHY.md'
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by '\n### [' to get blocks, but note that the first part before the first '### [' is irrelevant
    blocks = re.split(r'\n### \[', content)
    new_entries = []
    for block in blocks[1:]:  # Skip the first part
        # Extract the key from the first line of the block
        first_line_end = block.find('\n')
        if first_line_end == -1:
            continue
        first_line = block[:first_line_end]
        # Extract key: pattern [F01]
        key_match = re.search(r'\[([A-Z][0-9]+)\]', first_line)
        if not key_match:
            continue
        key = key_match.group(1)
        # Get all lines
        lines = block.split('\n')
        # The citation line is the second non-empty line after the first line? Actually, we saw pattern: line0: key line, line1: empty, line2: citation, line3: empty, line4: Use...
        # Let's find the first non-empty line after the first line that is not a header (doesn't start with '###')
        citation_line = None
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            if line.startswith('###'):
                break
            # We assume the citation line contains a year in parentheses and a dot
            if re.search(r'\(\d{4}\)', line) and '.' in line:
                citation_line = line
                break
        if citation_line is None:
            # Fallback: take the first non-empty line after the first line that is not a header
            for i in range(1, len(lines)):
                line = lines[i].strip()
                if not line:
                    continue
                if not line.startswith('###'):
                    citation_line = line
                    break
        if citation_line is None:
            print(f"Warning: Could not find citation line for key {key}")
            continue
        parsed = parse_citation_line(citation_line)
        if parsed is None:
            print(f"Warning: Could not parse citation for key {key}")
            continue
        parsed['key'] = key
        new_entries.append(parsed)
    
    print(f"Generated {len(new_entries)} new bibliography entries from markdown.")
    
    # Now write the BibTeX file
    bib_lines = []
    for entry in new_entries:
        key = entry['key']
        # Determine entry type: if journal is present -> article, else book
        entry_type = 'article' if entry.get('journal') else 'book'
        bib_lines.append(f'@{entry_type}{{{key},')
        for field in ['author', 'title', 'journal', 'volume', 'number', 'pages', 'year', 'doi']:
            value = entry.get(field, '')
            if value:
                bib_lines.append(f'  {field} = {{{value}}},')
        # Remove trailing comma from the last field line
        if bib_lines[-1].strip().endswith(','):
            bib_lines[-1] = bib_lines[-1].rstrip(',')
        bib_lines.append('}')
        bib_lines.append('')  # empty line between entries
    
    bib_content = '\n'.join(bib_lines)
    with open('paper/bibliography.bib', 'w', encoding='utf-8') as f:
        f.write(bib_content)
    
    # Let's also count the number of @ entries in the file to verify
    with open('paper/bibliography.bib', 'r', encoding='utf-8') as f:
        bib_content = f.read()
    num_entries = len(re.findall(r'@\w+{', bib_content))
    print(f"Number of @ entries in bibliography.bib: {num_entries}")
    
    # Now, we need to replace the old keys in the .tex files with the new keys.
    # We have a mapping from old key to new key? We need to know what the old keys were.
    # We can get the old keys from the original bibliography (from git) or we can assume that the old keys are the ones like sasmal2018, etc.
    # But we already have the original bibliography from the previous run? We can read the current bibliography.bib (which we just overwrote) but we lost the old one.
    # However, we can get the old keys from the .tex files by extracting all citation keys.
    # Let's do that: extract all keys from .tex files that match the pattern of the old keys (lowercase letters and digits).
    # Then we need to map each old key to the new key based on matching content.
    # But we already have a mapping from the original entries to the new entries by matching author, year, title.
    # We'll do that: parse the original bibliography from git, parse the new entries, and create a mapping.
    
    # Step: get original bibliography from git
    try:
        original_bib_content = subprocess.check_output(
            ['git', 'show', 'HEAD:paper/bibliography.bib'],
            stderr=subprocess.DEVNULL,
            text=True
        )
    except subprocess.CalledProcessError:
        print("Could not retrieve original bibliography from git. Proceeding without key replacement.")
        original_bib_content = ''
    
    # Parse original bibliography
    if original_bib_content:
        original_entries = parse_bibtex(original_bib_content)
        print(f"Parsed {len(original_entries)} original bibliography entries.")
        
        # Build a mapping from (normalized_author, normalized_title, year) to original key
        def normalize_author(author):
            author = author.lower()
            author = re.sub(r'\s+', ' ', author)
            return author.strip()
        
        def normalize_title(title):
            title = title.lower()
            title = re.sub(r'\s+', ' ', title)
            return title.strip()
        
        original_map = {}
        for entry in original_entries:
            fields = entry['fields']
            author = fields.get('author', '')
            title = fields.get('title', '')
            year = fields.get('year', '')
            key = entry['key']
            norm_author = normalize_author(author)
            norm_title = normalize_title(title)
            key_tuple = (norm_author, norm_title, year)
            if key_tuple not in original_map:
                original_map[key_tuple] = key
        
        # Map new entries to old keys
        old_to_new = {}
        for entry in new_entries:
            key = entry['key']
            author = entry.get('author', '')
            title = entry.get('title', '')
            year = entry.get('year', '')
            norm_author = normalize_author(author)
            norm_title = normalize_title(title)
            key_tuple = (norm_author, norm_title, year)
            old_key = original_map.get(key_tuple)
            if old_key:
                old_to_new[old_key] = key
            else:
                print(f"Warning: No matching original entry found for new key {key}")
        
        print(f"Created mapping for {len(old_to_new)} old keys to new keys.")
        
        # Walk through paper/sections and paper/main.tex
        for root, dirs, files in os.walk('paper'):
            for file in files:
                if file.endswith('.tex'):
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    # Replace each old key with the new key
                    for old_key, new_key in old_to_new.items():
                        # Use word boundaries to avoid partial matches
                        pattern = r'\b' + re.escape(old_key) + r'\b'
                        content = re.sub(pattern, new_key, content)
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
        print("Updated citation keys in .tex files.")
    else:
        print("Skipping key replacement because original bibliography not available.")
    
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
    
    # Final count
    with open('paper/bibliography.bib', 'r', encoding='utf-8') as f:
        bib_content = f.read()
    num_entries = len(re.findall(r'@\w+{', bib_content))
    print(f"Number of entries in bibliography.bib: {num_entries}")

if __name__ == '__main__':
    main()