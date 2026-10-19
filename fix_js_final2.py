# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('function openBook() {')
if start_idx != -1:
    end_idx = content.find('pf.loadFromHTML(', start_idx)
    if end_idx != -1:
        end_idx = content.find(';', end_idx) + 1
        
        # also remove updateNav and keyboard events if they are inside openBook or after it?
        # Actually I removed the nav buttons, so no need for updateNav or button clicks.
        # But wait! I replaced the whole openBook function previously?
        # Let's see what's after pf.loadFromHTML.
