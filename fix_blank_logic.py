# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
old_logic = '''  if (pagesArray.length % 2 !== 0) {
    let blank = document.createElement('div');
    blank.className = 'page page-inner';
    blank.innerHTML = '<div class="pg-head"></div><div style="display:flex;height:100%;align-items:center;justify-content:center;opacity:0.3;font-size:2rem;"><i class="fas fa-leaf"></i></div>';
    let backCover = pagesArray.pop();
    pagesArray.push(blank);
    pagesArray.push(backCover);
  }'''

new_logic = '''  if (pagesArray.length % 2 !== 0) {
    let blank = document.createElement('div');
    blank.className = 'page page-inner';
    blank.innerHTML = '<div class="pg-head"></div><div style="display:flex;height:100%;align-items:center;justify-content:center;opacity:0.3;font-size:2rem;"><i class="fas fa-leaf"></i></div>';
    pagesArray.push(blank);
  }'''

content = content.replace(old_logic, new_logic)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
