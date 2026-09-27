import re
import subprocess
import sys
import os

def parse_markdown_reference(text):
    """
    Parse a single reference entry from the markdown.
    Expected format:
    ### [F01] Caputo derivative
    Caputo, M. (1967). Linear models of dissipation whose Q is almost frequency independent—II. *Geophysical Journal International*, **13**(5), 529–539. DOI: `10.1111/j.1365-246X.1967.tb02303.x`.
    """
    lines = text.strip().split('\n')
    if not lines:
        return None
    # First line: ### [F01] Caputo derivative
    first_line = lines[0].strip()
    # Extract key: [F01]
    key_match = re.search(r'\[([A-Z][0-9]+)\]', first_line)
    if not key_match:
        return None
    key = key_match.group(1)
    # The rest of the lines (after the first line) until the next ### or end
    # We'll join the rest and then parse the citation.
    # But note: there might be a blank line after the first line? In the file, there is a blank line.
    # We'll skip empty lines until we find a non-empty line.
    citation_lines = []
    for line in lines[1:]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('###'):
            break
        citation_lines.append(stripped)
    citation = ' '.join(citation_lines)
    # Now parse the citation string.
    # We'll extract year, author, title, journal, volume, number, pages, doi.
    # Year: look for (yyyy)
    year_match = re.search(r'\((\d{4})\)', citation)
    if not year_match:
        return None
    year = year_match.group(1)
    # Author: everything before the year, but remove trailing dot and spaces.
    author_part = citation[:year_match.start()].strip()
    # Remove trailing dot if present
    if author_part.endswith('.'):
        author = author_part[:-1].strip()
    else:
        author = author_part
    # The part after the year
    after_year = citation[year_match.end():].strip()
    # Remove leading dot and space if present
    if after_year.startswith('. '):
        after_year = after_year[2:]
    elif after_year.startswith('.'):
        after_year = after_year[1:]
    # Now we look for the journal in *italics*
    journal_match = re.search(r'\*([^*]+)\*', after_year)
    if not journal_match:
        # Maybe it's a book without journal? Then we look for the title in italics? Actually, for a book, the title is in italics.
        # We'll assume the first italicized part is the title for a book, and journal for an article.
        # We'll need to differentiate by looking for volume and number pattern.
        pass
    journal = journal_match.group(1) if journal_match else ''
    # Title: everything between the year and the journal marker, but we need to remove the trailing dot.
    # Actually, the title ends before the journal marker, and there is a '. ' before the journal?
    # Let's find the position of the journal marker.
    journal_start = journal_match.start() if journal_match else -1
    journal_end = journal_match.end() if journal_match else -1
    if journal_start != -1:
        title_part = after_year[:journal_start].strip()
        # Remove trailing dot
        if title_part.endswith('.'):
            title = title_part[:-1].strip()
        else:
            title = title_part
        after_journal = after_year[journal_end:].strip()
    else:
        # No journal, so the whole after_year might be the title? But we already removed the year.
        # Actually, for a book, the title is in italics. So we should look for italics for the title.
        # Let's change approach: we'll look for all italic parts.
        pass
    # For simplicity, let's assume the format is consistent: author (year). Title. *Journal*, **vol**(num), pages. DOI: `doi`
    # We'll try to extract volume, number, pages, doi from after_journal.
    # Volume and number: **vol**(num)
    vol_issue_match = re.search(r'\*\*(\d+)\*\*\((\d+)\)', after_journal)
    if vol_issue_match:
        volume = vol_issue_match.group(1)
        number = vol_issue_match.group(2)
        # Remove this part
        after_journal = after_journal.replace(vol_issue_match.group(0), '', 1)
    else:
        # Just volume: **vol**
        vol_match = re.search(r'\*\*(\d+)\*\*', after_journal)
        if vol_match:
            volume = vol_match.group(1)
            number = ''
            after_journal = after_journal.replace(vol_match.group(0), '', 1)
        else:
            volume = ''
            number = ''
    # Pages: look for digits separated by en dash or hyphen
    pages_match = re.search(r'(\d+[\s\u2013-]\d+)', after_journal)
    if pages_match:
        pages = pages_match.group(1).strip()
        after_journal = after_journal.replace(pages_match.group(0), '', 1)
    else:
        pages = ''
    # DOI: look for `...`
    doi_match = re.search(r'`([^`]+)`', after_journal)
    if doi_match:
        doi = doi_match.group(1)
    else:
        doi = ''
    # Determine entry type: if journal is not empty, it's an article, else book.
    entry_type = 'article' if journal else 'book'
    # For book, the journal field is actually the title? Wait, we already have title.
    # For book, we might have publisher, ISBN, etc. But we don't have that in the citation.
    # We'll just put the journal in the 'journal' field for article, and for book we might put it in 'title'? Actually, we already have title.
    # Let's return the fields we have.
    return {
        'key': key,
        'type': entry_type,
        'author': author,
        'title': title,
        'journal': journal,
        'volume': volume,
        'number': number,
        'pages': pages,
        'year': year,
        'doi': doi
    }

def main():
    md_path = '17_BIBLIOGRAPHY.md'
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Split by '\n### [' to get blocks
    blocks = re.split(r'\n### \[', content)
    entries = []
    for block in blocks[1:]:  # Skip the first part before first '### ['
        lines = block.split('\n')
        # First line is like "F01] Caputo derivative"
        first_line = lines[0].strip()
        # Extract key: take the part before the first space and remove the trailing ']'
        key = first_line.split()[0].rstrip(']')
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
        # Parse the citation line
        parsed = parse_markdown_reference(citation_line)
        if parsed is None:
            print(f"Warning: Could not parse citation for key {key}", file=sys.stderr)
            continue
        # Override the key from the parsed one (should be the same)
        parsed['key'] = key
        entries.append(parsed)
    print(f"Generated {len(entries)} bibliography entries from markdown.")
    # Write BibTeX file
    bib_lines = []
    for entry in entries:
        key = entry['key']
        entry_type = entry['type']
        bib_lines.append(f'@{entry_type}{{{key},')
        # For article: author, title, journal, volume, number, pages, year, doi
        # For book: author, title, year, publisher, isbn, etc. But we don't have publisher and ISBN separately.
        # We'll output what we have.
        fields = []
        if entry.get('author'):
            fields.append(f'author = {{{entry["author"]}}}')
        if entry.get('title'):
            fields.append(f'title = {{{entry["title"]}}}')
        if entry.get('journal'):
            fields.append(f'journal = {{{entry["journal}}')
        if entry.get('volume'):
            fields.append(f'volume = {{{entry["volume"]}}}')
        if entry.get('number'):
            fields.append(f'number = {{{entry["number"]}}}')
        if entry.get('pages'):
            fields.append(f'pages = {{{entry["pages"]}}}')
        if entry.get('year'):
            fields.append(f'year = {{{entry["year"]}}}')
        if entry.get('doi'):
            fields.append(f'doi = {{{entry["doi"]}}}')
        # For book, we might want to add publisher and isbn if we had them.
        # We'll just output the fields we have.
        for i, field in enumerate(fields):
            if i == len(fields) - 1:
                bib_lines.append(f'  {field}')
            else:
                bib_lines.append(f'  {field},')
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
    # Now we need to update the citation keys in .tex files.
    # But note: the keys in the new bibliography are the same as the old keys (F01, F02, etc.)
    # However, the old bibliography had different keys (like sasmal2018). We need to map from the old keys to the new keys.
    # But wait: the current .tex files are still using the old keys? Let's check.
    # We'll get the original bibliography from git to see what keys are used in the .tex files.
    try:
        original_bib_content = subprocess.check_output(
            ['git', 'show', 'HEAD:paper/bibliography.bib'],
            stderr=subprocess.DEVNULL,
            text=True
        )
    except subprocess.CalledProcessError:
        print("Could not retrieve original bibliography from git. Skipping key replacement.")
        original_bib_content = ""
    if original_bib_content:
        # Parse original bibliography to get mapping from (author, title, year) to old key
        # We'll use the same parsing function but for BibTeX.
        def parse_bibtex_simple(content):
            entries = []
            blocks = re.split(r'\n@', content)
            for block in blocks[1:]:
                block = block.strip()
                if not block:
                    continue
                # Extract type and key
                match = re.match(r'@(\w+)\s*\{\s*([^,]+)', block)
                if not match:
                    continue
                entry_type = match.group(1)
                key = match.group(2).strip()
                # Find the matching brace
                start_brace = block.find('{')
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
                    continue
                field_str = block[start_brace+1:end_brace].strip()
                # Parse fields
                fields = {}
                field_pattern = re.compile(r'(\w+)\s*=\s*{([^}]*)}')
                for match in field_pattern.finditer(field_str):
                    field_name = match.group(1).lower()
                    field_value = match.group(2).strip()
                    fields[field_name] = field_value
                entries.append({
                    'type': entry_type,
                    'key': key,
                    'fields': fields
                })
            return entries
        original_entries = parse_bibtex_simple(original_bib_content)
        # Build mapping from (author, title, year) to old key
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
            signature = (norm_author, norm_title, year)
            if signature not in original_map:
                original_map[signature] = key
        # Map new entries to old keys
        old_to_new = {}
        for entry in entries:
            author = entry.get('author', '')
            title = entry.get('title', '')
            year = entry.get('year', '')
            key = entry['key']
            norm_author = normalize_author(author)
            norm_title = normalize_title(title)
            signature = (norm_author, norm_title, year)
            old_key = original_map.get(signature)
            if old_key:
                old_to_new[old_key] = key
            else:
                print(f"Warning: No matching original entry found for new key {key}")
        print(f"Created mapping for {len(old_to_new)} old keys to new keys.")
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