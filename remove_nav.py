# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div class="book-nav">.*?</div>\s*</div><!-- #bookScreen -->', '</div><!-- #bookScreen -->', content, flags=re.DOTALL)
content = re.sub(r'\.book-nav\{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'\.nav-btn\{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'\.nav-info\{.*?\}', '', content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
