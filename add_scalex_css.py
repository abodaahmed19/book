# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
content = re.sub(r'#flipBook\s*\{', '#flipBook{\n  transform: scaleX(-1);', content)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
