import re

def debug_parse_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by '\n### [' to get blocks
    blocks = re.split(r'\n### \[', content)
    print(f"Number of blocks: {len(blocks)}")
    
    for i, block in enumerate(blocks[1:6]):  # Look at first 5 blocks after the initial part
        print(f"\n=== Block {i+1} ===")
        lines = block.split('\n')
        for j, line in enumerate(lines):
            print(f"  {j}: {repr(line)}")
        
        # Now try to extract the key and citation line as in our function
        first_line_end = block.find('\n')
        if first_line_end == -1:
            print("  No newline in block")
            continue
        first_line = block[:first_line_end]
        key_match = re.search(r'\[([A-Z][0-9]+)\]', first_line)
        if not key_match:
            print("  No key found in first line")
            continue
        key = key_match.group(1)
        print(f"  Key: {key}")
        
        # Get the lines after the first line
        rest_lines = [line.strip() for line in block[first_line_end+1:].split('\n') if line.strip()]
        print(f"  Non-empty lines after first line: {rest_lines}")
        
        citation_line = None
        for line in rest_lines:
            if line.startswith('###'):
                continue
            if re.search(r'\(\d{4}\)', line) and '.' in line:
                citation_line = line
                break
        if citation_line is None:
            for line in rest_lines:
                if not line.startswith('###'):
                    citation_line = line
                    break
        print(f"  Selected citation line: {repr(citation_line)}")

if __name__ == '__main__':
    debug_parse_md('17_BIBLIOGRAPHY.md')