# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'function toggleFS\(\) \{.*?\n\}', '', content, flags=re.DOTALL)
content = re.sub(r'function closePage\(\) \{.*?\n\}', '', content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
