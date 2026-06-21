import re
import glob

def escape_mathjax(match):
    # This function takes a MathJax block e.g. \( ... \) and escapes < and >
    inner = match.group(1)
    inner = inner.replace('<', '&lt;').replace('>', '&gt;')
    return r'\(' + inner + r'\)'

for file in glob.glob("generate_chapter_*.py"):
    with open(file, 'r') as f:
        content = f.read()
    
    # We replace \( ... \)
    new_content = re.sub(r'\\\((.*?)\\\)', escape_mathjax, content, flags=re.DOTALL)
    
    with open(file, 'w') as f:
        f.write(new_content)

print("Fixed generators!")
