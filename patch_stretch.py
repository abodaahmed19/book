# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Update openBook size setting
content = re.sub(
    r"size:\s*'fixed',",
    "size:       'stretch',",
    content
)

# Update flipBook CSS to fill the screen
content = re.sub(
    r"#flipBook\{",
    "#flipBook{\n  width: 100vw;\n  height: 100vh;",
    content
)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
