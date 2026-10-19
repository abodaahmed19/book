# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
content = re.sub(
    r'\.book-wrapper\s*\{.*?\}',
    '',
    content, flags=re.DOTALL
)

content = content.replace(
    '#coverScreen{',
    '.book-wrapper { filter: drop-shadow(0 30px 60px rgba(0,0,0,0.8)); }\n#coverScreen{'
)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
