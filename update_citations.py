import re
import os
import subprocess

def parse_bibliography(filename):
    """Parse the bibliography markdown file.
    Returns a dict mapping (author_last_lower, year) -> bib_key
    Also returns a set of all bib_keys for quick lookup.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    mapping = {}  # (author_last, year) -> key
    bib_keys = set()
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for header line
        header_match = re.match(r'### \[([A-Z0-9]+)\]', line)
        if header_match:
            key = header_match.group(1)
            bib_keys.add(key)
            # Find the next non-empty line that is not a header
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j >= len(lines):
                break
            author_line = lines[j].strip()
            # Extract author part before the first comma
            if ',' in author_line:
                author_part = author_line.split(',')[0].strip()
            else:
                # If no comma, take the first word(s) until a space or parenthesis?
                # We'll take the first word
                author_part = author_line.split()[0] if author_line.split() else ''
            # Remove any trailing period
            author_part = author_part.rstrip('.')
            # Extract year: look for parentheses with four digits
            year_match = re.search(r'\((\d{4})\)', author_line)
            if year_match:
                year = year_match.group(1)
                author_last = author_part.lower()
                mapping[(author_last, year)] = key
            # Move i to j to continue after the author line? We'll just increment i by 1 and continue.
            i = j
        i += 1
    return mapping, bib_keys

def extract_author_year_from_key(key):
    """Extract author part and year from a citation key like 'baik2020optimal'.
    Returns (author_part, year) where author_part is the string before the year (with trailing underscore removed).
    """
    year_match = re.search(r'(\d{4})', key)
    if not year_match:
        return None, None
    year = year_match.group(1)
    author_part = key[:year_match.start()].rstrip('_')
    return author_part, year

def process_tex_file(filepath, bib_map, bib_keys):
    """Read a .tex file, replace citation keys, and write back if changed."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find \cite{...}, \citep{...}, \citet{...}, etc.
    # We'll capture the content inside the braces.
    pattern = re.compile(r'\\cite[pt]?\*?\s*\{([^}]+)\}')
    
    def replace_func(match):
        inner = match.group(1)
        # Split by commas to handle multiple citations
        parts = [part.strip() for part in inner.split(',')]
        new_parts = []
        for part in parts:
            if not part:
                continue
            # Check if this part is already a known bib key (like F01, O05)
            if part in bib_keys:
                new_parts.append(part)
                continue
            # Try to map the old key
            author_part, year = extract_author_year_from_key(part)
            if author_part is None or year is None:
                # Cannot extract, keep as is? Or mark as needed?
                # We'll mark as needed with the part as claim
                new_parts.append(f'[[CITE-NEEDED: {part}]]')
                continue
            # Look up in bibliography
            new_key = bib_map.get((author_part.lower(), year))
            if new_key:
                new_parts.append(new_key)
            else:
                # Not found, mark as needed
                new_parts.append(f'[[CITE-NEEDED: {part}]]')
        return ', '.join(new_parts)
    
    new_content = pattern.sub(replace_func, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    bib_file = '17_BIBLIOGRAPHY.md'
    bib_map, bib_keys = parse_bibliography(bib_file)
    print(f"Loaded {len(bib_map)} entries from bibliography.")
    print(f"Sample bib keys: {list(bib_keys)[:10]}")
    
    # Find all .tex files in paper/sections and paper/main.tex
    tex_files = []
    for root, dirs, files in os.walk('paper'):
        for f in files:
            if f.endswith('.tex'):
                tex_files.append(os.path.join(root, f))
    
    print(f"Found {len(tex_files)} .tex files to process.")
    
    changed_files = []
    for tf in tex_files:
        if process_tex_file(tf, bib_map, bib_keys):
            changed_files.append(tf)
            print(f"Updated: {tf}")
    
    print(f"\nTotal files changed: {len(changed_files)}")
    if changed_files:
        print("Changed files:")
        for f in changed_files:
            print(f"  {f}")
    
    # Optionally, run a quick check to see if the bibliography file is up to date?
    # We assume it's already correct from previous turn.
    
    # Try to compile the paper to see if it works (optional, but good to check)
    # We'll run a quick make or latexmk if available, but we don't want to take too long.
    # Let's just check if main.tex exists and run a quick pdflatex on it (non-stop mode) and see if there are any obvious errors.
    # We'll do this only if there were changes.
    if changed_files:
        print("\nAttempting to compile the paper to check for errors...")
        # Change to the paper directory
        orig_dir = os.getcwd()
        os.chdir('paper')
        # Run pdflatex on main.tex, non-stop mode, redirect output to a log file
        result = subprocess.run(['pdflatex', '-interaction=nonstop-mode', 'main.tex'], 
                                capture_output=True, text=True, timeout=30)
        os.chdir(orig_dir)
        if result.returncode != 0:
            print("Compilation failed or had errors. See output below:")
            print(result.stdout[-500:])  # Show last 500 chars of stdout
            print(result.stderr[-500:])  # Show last 500 chars of stderr
        else:
            print("Compilation succeeded (or at least no errors reported).")
    else:
        print("No files changed, skipping compilation.")

if __name__ == '__main__':
    main()