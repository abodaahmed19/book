# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# restore fixed size
content = content.replace("size:       'stretch',", "size:       'fixed',")
content = re.sub(r'#flipBook\{\n  width: 100vw;\n  height: 100vh;', '#flipBook{', content)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
