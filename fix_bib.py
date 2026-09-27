import re
import os
import subprocess
import sys

def parse_citation_line(line):
    """Parse a line like:
    Caputo, M. (1967). Linear models of dissipation whose Q is almost frequency independent—II. *Geophysical Journal International*, **13**(5), 529–539. DOI: `10.1111/j.1365-246X.1967.tb02303.x`.
    Returns a dict with keys: author, year, title, journal, volume, number, pages, doi
    """
    # Extract year: look for (yyyy)
    year_match = re.search(r'\((\d{4})\)', line)
    if not year_match:
        return None
    year = year_match.group(1)
    
    # Split into parts: before year and after year
    before_year = line[:year_match.start()].strip()
    after_year = line[year_match.end():].strip()
    
    # Author is before_year (remove trailing dot if any)
    author = before_year.rstrip('.')
    
    # The rest after year should start with title, then journal, etc.
    # We look for the journal in *italics*
    journal_match = re.search(r'\*([^*]+)\*', after_year)
    if not journal_match:
        return None
    journal = journal_match.group(1)
    
    # Title is everything between the year and the journal marker, but we need to remove the trailing dot and space
    # Actually, the title ends before the journal marker, but there is a '. ' before the journal?
    # Let's find the position of the journal marker and then look backwards for the title.
    journal_start = journal_match.start()
    journal_end = journal_match.end()
    
    # The part before the journal marker is: after_year[:journal_start]
    # This should end with the title and then a '. ' (or just '.')
    title_and_dot = after_year[:journal_start].strip()
    # Remove trailing dot and any spaces
    if title_and_dot.endswith('.'):
        title = title_and_dot[:-1].strip()
    else:
        title = title_and_dot  # fallback
    
    # The part after the journal marker
    after_journal = after_year[journal_end:].strip()
    
    # Now extract volume and number: look for **vol**(num)
    vol_issue_match = re.search(r'\*\*(\d+)\*\*\((\d+)\)', after_journal)
    if vol_issue_match:
        volume = vol_issue_match.group(1)
        number = vol_issue_match.group(2)
        # Remove this part from after_journal
        after_journal = after_journal.replace(vol_issue_match.group(0), '', 1)
    else:
        # Look for just volume: **vol**
        vol_match = re.search(r'\*\*(\d+)\*\*', after_journal)
        if vol_match:
            volume = vol_match.group(1)
            number = ''
            after_journal = after_journal.replace(vol_match.group(0), '', 1)
        else:
            volume = ''
            number = ''
    
    # Extract pages: look for digits separated by en dash or hyphen
    pages_match = re.search(r'(\d+[\s\u2013-]\d+)', after_journal)
    if pages_match:
        pages = pages_match.group(1).strip()
        after_journal = after_journal.replace(pages_match.group(0), '', 1)
    else:
        pages = ''
    
    # Extract DOI: look for `...`
    doi_match = re.search(r'`([^`]+)`', after_journal)
    if doi_match:
        doi = doi_match.group(1)
    else:
        doi = ''
    
    # Clean up fields
    author = author.strip()
    title = title.strip()
    journal = journal.strip()
    volume = volume.strip()
    number = number.strip()
    pages = pages.strip()
    doi = doi.strip()
    
    return {
        'author': author,
        'year': year,
        'title': title,
        'journal': journal,
        'volume': volume,
        'number': number,
        'pages': pages,
        'doi': doi
    }

def main():
    md_path = '17_BIBLIOGRAPHY.md'
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by '\n### [' to get blocks, but note that the first part before the first '### [' is irrelevant
    blocks = re.split(r'\n### \[', content)
    entries = []
    for block in blocks[1:]:  # Skip the first part before first '### ['
        lines = block.split('\n')
        # First line is like "F01] Caputo derivative"
        first_line = lines[0].strip()
        # Extract key: everything before the first space
        key_end = first_line.find(' ')
        if key_end == -1:
            key = first_line.rstrip(']')
        else:
            key = first_line[:key_end]
        # Find citation line: first non-empty line after the first line that is not a header and contains a year in parentheses
        citation_line = None
        for line in lines[1:]:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith('###'):
                break
            if re.search(r'\(\d{4}\)', stripped) and '.' in stripped:
                citation_line = stripped
                break
        if citation_line is None:
            print(f"Warning: Could not find citation line for key {key}", file=sys.stderr)
            continue
        parsed = parse_citation_line(citation_line)
        if parsed is None:
            print(f"Warning: Could not parse citation for key {key}", file=sys.stderr)
            continue
        parsed['key'] = key
        entries.append(parsed)
    
    print(f"Generated {len(entries)} bibliography entries from markdown.")
    
    # Write BibTeX file
    bib_lines = []
    for entry in entries:
        key = entry['key']
        entry_type = 'article' if entry.get('journal') else 'book'
        bib_lines.append(f'@{entry_type}{{{key},')
        for field in ['author', 'title', 'journal', 'volume', 'number', 'pages', 'year', 'doi']:
            value = entry.get(field, '')
            if value:
                bib_lines.append(f'  {field} = {{{value}}},')
        # Remove trailing comma from last line
        if bib_lines[-1].strip().endswith(','):
            bib_lines[-1] = bib_lines[-1].rstrip(',')
        bib_lines.append('}')
        bib_lines.append('')  # empty line between entries
    
    bib_content = '\n'.join(bib_lines)
    with open('paper/bibliography.bib', 'w', encoding='utf-8') as f:
        f.write(bib_content)
    
    # Count entries
    with open('paper/bibliography.bib', 'r', encoding='utf-8') as f:
        bib_content = f.read()
    num_entries = len(re.findall(r'@\\w+{', bib_content))
    print(f"Number of @ entries in bibliography.bib: {num_entries}")
    
    # Now, we need to replace old keys in .tex files with new keys.
    # Get original bibliography from git
    try:
        original_bib_content = subprocess.check_output(
            ['git', 'show', 'HEAD:paper/bibliography.bib'],
            stderr=subprocess.DEVNULL,
            text=True
        )
    except subprocess.CalledProcessError:
        print("Could not retrieve original bibliography from git. Proceeding without key replacement.")
        original_bib_content = ''
    
    # Parse original bibliography to get mapping from (author, title, year) to old key
    def parse_bibtex(content):
        entries = []
        # Split by '@'
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
            field_str = after_brace[comma+1:]
            # Parse fields: look for \w+ = { ... }
            field_pattern = re.compile(r'(\w+)\s*=\s*{([^}]*)}')
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
    
    if original_bib_content:
        original_entries = parse_bibtex(original_bib_content)
        print(f"Parsed {len(original_entries)} original bibliography entries.")
        # Build mapping from normalized (author, title, year) to original key
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
        for entry in entries:
            author = entry.get('author', '')
            title = entry.get('title', '')
            year = entry.get('year', '')
            key = entry['key']
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
                    # Replace each old key with new key
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
    num_entries = len(re.findall(r'@\\w+{', bib_content))
    print(f"Number of entries in bibliography.bib: {num_entries}")

if __name__ == '__main__':
    main()