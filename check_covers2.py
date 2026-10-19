# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.rfind('</div><!-- #flipBook -->')
print(text[idx-500:idx+100])
