# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("size:       'fixed',", "size:       'stretch',")
if '#flipBook{\n  width: 100vw;\n  height: 100vh;' not in content:
    content = content.replace('#flipBook{', '#flipBook{\n  width: 100vw;\n  height: 100vh;')

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
