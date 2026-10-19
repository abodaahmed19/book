# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Fixed UI buttons block
content = re.sub(r'<!-- Fixed UI buttons -->.*?<!-- Messages -->', '<!-- Messages -->', content, flags=re.DOTALL)

# 2. Remove CSS for them
content = re.sub(r'#btnFS\{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'#btnAdmin\{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'#btnClose\{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'\.fixed-btn\{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'\.fixed-btn:hover\{.*?\}', '', content, flags=re.DOTALL)
content = content.replace('/* ── FIXED BUTTONS ── */', '')

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
