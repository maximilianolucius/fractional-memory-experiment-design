import re
with open('17_BIBLIOGRAPHY.md', 'r') as f:
    content = f.read()
print('Total length:', len(content))
# Split by '\n### ['
blocks = re.split(r'\n### \[', content)
print('Number of blocks:', len(blocks))
for i, block in enumerate(blocks[:5]):
    print(f'Block {i} first 200 chars:', repr(block[:200]))