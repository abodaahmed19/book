# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

old_drag = '''  // Custom click logic to satisfy LTR digital expectations for RTL reading
  let isDragging = false;
  const fb = document.getElementById('flipBook');
  fb.addEventListener('pointerdown', () => { isDragging = false; });
  fb.addEventListener('pointermove', () => { isDragging = true; });
  
  fb.addEventListener('pointerup', (e) => {
    if (isDragging) return;'''

new_drag = '''  // Custom click logic to satisfy LTR digital expectations for RTL reading
  let startX = 0;
  let startY = 0;
  let isDragging = false;
  const fb = document.getElementById('flipBook');
  
  fb.addEventListener('pointerdown', (e) => { 
    startX = e.clientX; 
    startY = e.clientY; 
    isDragging = false; 
  });
  
  fb.addEventListener('pointermove', (e) => { 
    if (Math.abs(e.clientX - startX) > 5 || Math.abs(e.clientY - startY) > 5) {
      isDragging = true;
    }
  });
  
  fb.addEventListener('pointerup', (e) => {
    if (isDragging) return;'''

content = content.replace(old_drag, new_drag)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
