# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="flipBook"')
print(text[idx:idx+1000])
