# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's replace the block using index or a simpler regex
content = re.sub(r'\.page\s*\{[^\}]+\}', '.page{\n  background: linear-gradient(180deg, #fdfaf3 0%, #f6f0df 100%);\n  font-family:\'Cairo\',sans-serif;\n  overflow:hidden;\n  position:relative;\n  box-shadow: inset 0 0 20px rgba(0,0,0,0.05);\n  border: 1px solid rgba(0,0,0,0.08);\n  border-radius: 4px;\n}\n.page::before {\n  content: "";\n  position: absolute;\n  top: 0; bottom: 0; left: 0; right: 0;\n  box-shadow: inset 0 0 10px rgba(201,162,39,0.1);\n  pointer-events: none;\n}', content, count=1)

content = re.sub(r'\.page-inner\s*\{[^\}]+\}', '.page-inner{\n  padding:25px 25px 20px;\n  display:flex;flex-direction:column;\n  height: 100%;\n}', content, count=1)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
