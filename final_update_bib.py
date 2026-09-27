import re
import os
import subprocess
import json

def normalize_author(author):
    """Normalize author string for comparison."""
    if not author:
        return ""
    # Convert to lower case
    author = author.lower()
    # Replace multiple spaces with a single space
    author = re.sub(r'\s+', ' ', author)
    # Remove extra spaces at the start and end
    author = author.strip()
    # Remove punctuation at the end (like periods, commas) but keep intra-word punctuation
    author = re.sub(r'[.,;:]+$', '', author)
    return author

def normalize_title(title):
    """Normalize title string for comparison."""
    if not title:
        return ""
    # Convert to lower case
    title = title.lower()
    # Replace multiple spaces with a single space
    title = re.sub(r'\s+', ' ', title)
    # Remove extra spaces at the start and end
    title = title.strip()
    # Remove punctuation at the end (like periods, commas) but keep intra-word punctuation
    title = re.sub(r'[.,;:]+$', '', title)
    # Remove articles at the beginning? Might be too aggressive, but we can try.
    # For now, we leave it.
    return title

def parse_citation_line(line):
    """
    Parse a citation line from the bibliography markdown.
    Returns a dictionary with keys: author, year, title, journal, volume, number, pages, doi.
    If a field cannot be found, it will be an empty string.
    """
    # Initialize all fields
    result = {
        'author': '',
        'year': '',
        'title': '',
        'journal': '',
        'volume': '',
        'number': '',
        'pages': '',
        'doi': ''
    }
    
    if not line:
        return result
    
    # Try to split by '. ' but we need to be careful about abbreviations.
    # We'll use a regex to split at the first '. ' that is followed by a space and then an opening parenthesis for the year?
    # Actually, the author part ends before the year in parentheses.
    # Let's try to extract the year first: look for a four-digit number in parentheses.
    year_match = re.search(r'\((\d{4})\)', line)
    if not year_match:
        # If we can't find a year in parentheses, we cannot parse.
        return result
    year = year_match.group(1)
    year_pos = year_match.start()
    
    # The author is everything before the year, but we need to strip trailing spaces and punctuation.
    author_part = line[:year_pos].strip()
    # Remove any trailing period or comma that might be part of the author separator.
    author_part = re.sub(r'[.,;:]+$', '', author_part)
    result['author'] = author_part
    result['year'] = year
    
    # The rest of the line after the year and the closing parenthesis.
    rest = line[year_match.end():].strip()
    # If the rest starts with a period and space, remove them.
    if rest.startswith('. '):
        rest = rest[2:]
    elif rest.startswith('.'):
        rest = rest[1:]
    
    # Now, the title is likely the first part of the rest, but it might be in italics.
    # We'll look for the first occurrence of a period that is followed by a space and then either:
    #   - a word in asterisks (indicating a journal or book title)
    #   - a capital letter (indicating the start of a proper noun, like a journal name)
    #   - a digit (indicating a volume number)
    #   - the word 'In' or 'doi' or 'ISBN'
    # But this is complex.
    
    # Instead, we'll split the rest by '. ' and take the first element as the title candidate.
    # We'll then check if the title candidate is wrapped in asterisks (italic) and remove them.
    parts = re.split(r'\.\s+', rest)
    if not parts:
        result['title'] = ""
        return result
    
    title_candidate = parts[0].strip()
    # Remove surrounding asterisks if present (italic)
    if title_candidate.startswith('*') and title_candidate.endswith('*'):
        title_candidate = title_candidate[1:-1]
    result['title'] = title_candidate
    
    # The remaining parts are the publication info.
    pub_info = '. '.join(parts[1:]) if len(parts) > 1 else ""
    
    # Now try to extract journal, volume, number, pages, doi from pub_info.
    # We'll look for journal: text in asterisks.
    journal_match = re.search(r'\*([^*]+)\*', pub_info)
    if journal_match:
        result['journal'] = journal_match.group(1)
        # Remove this occurrence from pub_info to avoid double counting
        pub_info = pub_info.replace(journal_match.group(0), '', 1)
    
    # Look for volume and number: pattern like **vol**(num) or vol(num) or vol. num
    vol_match = re.search(r'\*\*(\d+)\*\*\((\d+)\)', pub_info)
    if vol_match:
        result['volume'] = vol_match.group(1)
        result['number'] = vol_match.group(2)
        pub_info = pub_info.replace(vol_match.group(0), '', 1)
    else:
        # Look for just volume: **vol**
        vol_match = re.search(r'\*\*(\d+)\*\*', pub_info)
        if vol_match:
            result['volume'] = vol_match.group(1)
            pub_info = pub_info.replace(vol_match.group(0), '', 1)
        # Look for volume without asterisks: vol(num) or vol. num
        vol_match = re.search(r'(\d+)\s*[\(\.](\d+)', pub_info)
        if vol_match:
            result['volume'] = vol_match.group(1)
            result['number'] = vol_match.group(2)
            pub_info = pub_info.replace(vol_match.group(0), '', 1)
    
    # Look for pages: pattern like pp. xxx-yyy or xxx-yyy
    pages_match = re.search(r'pp\.\s*(\d+[\-\u2013]\d+)', pub_info, re.IGNORECASE)
    if pages_match:
        result['pages'] = pages_match.group(1)
        pub_info = pub_info.replace(pages_match.group(0), '', 1)
    else:
        pages_match = re.search(r'(\d+[\-\u2013]\d+)', pub_info)
        if pages_match:
            result['pages'] = pages_match.group(1)
            pub_info = pub_info.replace(pages_match.group(0), '', 1)
    
    # Look for DOI: `...`
    doi_match = re.search(r'`([^`]+)`', pub_info)
    if doi_match:
        result['doi'] = doi_match.group(1)
        pub_info = pub_info.replace(doi_match.group(0), '', 1)
    
    # Look for ISBN: `...`
    isbn_match = re.search(r'ISBN\s*:?\s*`([^`]+)`', pub_info, re.IGNORECASE)
    if isbn_match:
        # We don't have an ISBN field in our standard BibTeX, but we can put it in note if needed.
        # For now, we'll ignore it.
        pass
    
    # Clean up the pub_info string (remove extra spaces and dots)
    pub_info = re.sub(r'\s+', ' ', pub_info).strip()
    pub_info = re.sub(r'[.,;:]+$', '', pub_info)
    # We could put the remaining pub_info in a note field, but we don't have a note field in our standard.
    # We'll ignore it for now.
    
    return result

def parse_bibtex(content):
    """Parse BibTeX content and return a list of dicts with key and fields."""
    entries = []
    # Split by '@' and skip the first empty part
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
    # Step 1: Parse the markdown file to get new entries
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
        # Get the lines after the first line
        lines = [line.strip() for line in block[first_line_end+1:].split('\n') if line.strip()]
        if not lines:
            continue
        # The citation line is the first non-empty line that is not a header
        citation_line = None
        for line in lines:
            if line.startswith('###'):
                continue
            # We assume the citation line contains a year in parentheses and a dot
            if re.search(r'\(\d{4}\)', line) and '.' in line:
                citation_line = line
                break
        if citation_line is None:
            # Fallback: take the first non-header line
            for line in lines:
                if not line.startswith('###'):
                    citation_line = line
                    break
        if citation_line is None:
            print(f"Warning: Could not find citation line for key {key}")
            continue
        parsed = parse_citation_line(citation_line)
        if not parsed['author'] or not parsed['year'] or not parsed['title']:
            print(f"Warning: Could not parse citation for key {key}: {parsed}")
            continue
        parsed['key'] = key
        new_entries.append(parsed)
    
    print(f"Generated {len(new_entries)} new bibliography entries from markdown.")
    
    # Step 2: Get the original bibliography from git
    try:
        original_bib_content = subprocess.check_output(
            ['git', 'show', 'HEAD:paper/bibliography.bib'],
            stderr=subprocess.DEVNULL,
            text=True
        )
    except subprocess.CalledProcessError:
        print("Could not retrieve original bibliography from git. Proceeding without key replacement.")
        original_bib_content = ''
    
    original_entries = []
    if original_bib_content:
        original_entries = parse_bibtex(original_bib_content)
        print(f"Parsed {len(original_entries)} original bibliography entries.")
    
    # Step 3: Build mapping from old key to new key by matching author, year, title
    old_to_new = {}
    if original_entries:
        # Build a lookup for original entries by (normalized_author, normalized_title, year)
        original_lookup = {}
        for entry in original_entries:
            fields = entry['fields']
            author = fields.get('author', '')
            title = fields.get('title', '')
            year = fields.get('year', '')
            key = entry['key']
            norm_author = normalize_author(author)
            title_norm = normalize_title(title)
            key_tuple = (norm_author, title_norm, year)
            if key_tuple not in original_lookup:
                original_lookup[key_tuple] = key
        
        # For each new entry, try to find a matching original entry
        for entry in new_entries:
            key = entry['key']
            author = entry.get('author', '')
            title = entry.get('title', '')
            year = entry.get('year', '')
            norm_author = normalize_author(author)
            title_norm = normalize_title(title)
            key_tuple = (norm_author, title_norm, year)
            old_key = original_lookup.get(key_tuple)
            if old_key:
                old_to_new[old_key] = key
            else:
                print(f"Warning: No matching original entry found for new key {key}")
    
    print(f"Created mapping for {len(old_to_new)} old keys to new keys.")
    if old_to_new:
        print("Mapping:", json.dumps(old_to_new, indent=2))
    
    # Step 4: Generate the new bibliography.bib file with the new entries
    bib_lines = []
    for entry in new_entries:
        key = entry['key']
        # Determine entry type: if journal is present -> article, else book
        entry_type = 'article' if entry.get('journal') else 'book'
        bib_lines.append(f'@{entry_type}{{{key},')
        for field in ['author', 'title', 'journal', 'volume', 'number', 'pages', 'year', 'doi']:
            value = entry.get(field, '')
            if value:
                bib_lines[-1] == '.' and field not in ['doi']:  # Remove trailing period if present, except for DOI
                value = value[:-1]
            if value:
                # Escape any curly braces in the value? We'll assume they are already balanced.
                bib_lines.append(f'  {field} = {{{value}}},')
        # Remove trailing comma from the last field line
        if bib_lines[-1].strip().endswith(','):
            bib_lines[-1] = bib_lines[-1].rstrip(',')
        bib_lines.append('}')
        bib_lines.append('')  # empty line between entries
    
    bib_content = '\n'.join(bib_lines)
    with open('paper/bibliography.bib', 'w', encoding='utf-8') as f:
        f.write(bib_content)
    
    # Step 5: Replace old keys in .tex files with new keys
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
    
    # Step 6: Run bibtex and pdflatex to verify
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