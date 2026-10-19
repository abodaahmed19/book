# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("document.getElementById('btnClose').style.display = 'flex';", "")

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
