# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
old_click = '''  fb.addEventListener('click', (e) => {'''
new_click = '''  fb.addEventListener('pointerdown', (e) => {
    // If it's a click, we want to handle it ourselves. But pointerdown is the start of a drag too!
    // We can't stop propagation on pointerdown or swipe will break.
  });'''
