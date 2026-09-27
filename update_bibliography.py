import re
import sys

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

def main():
    md_path = '17_BIBLIOGRAPHY.md'
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by '\n### [' to get blocks, but note that the first part before the first '### [' is irrelevant
    blocks = re.split(r'\n### \[', content)
    entries = []
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
        # The citation line is the first non-empty line after the first line that is not a header
        lines = [line.strip() for line in block[first_line_end+1:].split('\n') if line.strip()]
        citation_line = None
        for line in lines:
            # Skip lines that are still headers (shouldn't happen, but safe)
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
            print(f"Warning: Could not find citation line for key {key}", file=sys.stderr)
            continue
        parsed = parse_citation_line(citation_line)
        if parsed is None:
            print(f"Warning: Could not parse citation for key {key}", file=sys.stderr)
            continue
        parsed['key'] = key
        entries.append(parsed)
    
    # Now write the BibTeX file
    bib_lines = []
    for entry in entries:
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
    
    print(f"Generated {len(entries)} bibliography entries.")
    
    # Let's also count the number of @ entries in the file to verify
    with open('paper/bibliography.bib', 'r', encoding='utf-8') as f:
        bib_content = f.read()
    num_entries = len(re.findall(r'@\w+{', bib_content))
    print(f"Number of @ entries in bibliography.bib: {num_entries}")

if __name__ == '__main__':
    main()