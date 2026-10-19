# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

old_click = '''  fb.addEventListener('click', (e) => {
    if (isDragging) return;
    if (pf.getState() !== 'read') return;
    
    const rect = fb.getBoundingClientRect();
    const x = e.clientX - rect.left;
    
    if (x > rect.width / 2) {
      // Clicked Right side -> User wants "Next/Forward"
      // Forward in our reversed DOM is flipPrev
      pf.flipPrev();
    } else {
      // Clicked Left side -> User wants "Prev/Backward"
      // Backward is flipNext
      pf.flipNext();
    }
  });'''

new_click = '''  fb.addEventListener('click', (e) => {
    if (isDragging) return;
    if (pf.getState() !== 'read') return;
    
    const rect = fb.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const current = pf.getCurrentPageIndex();
    
    if (x > rect.width / 2) {
      // Clicked Right side -> Forward (flipPrev)
      if (current > 0) {
        pf.flipPrev();
      }
    } else {
      // Clicked Left side -> Backward (flipNext)
      if (current < pf.getPageCount() - 2) {
        pf.flipNext();
      }
    }
  });'''

content = content.replace(old_click, new_click)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
