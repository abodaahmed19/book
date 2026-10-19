# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Remove the previous custom click block first
content = re.sub(r'  // Custom click logic.*?pf\.flipNext\(\);\n    \}\n  \}\);\n', '', content, flags=re.DOTALL)

safe_click = '''  pf.loadFromHTML(pagesArray);

  // Custom click logic to satisfy LTR digital expectations for RTL reading
  let isDragging = false;
  const fb = document.getElementById('flipBook');
  fb.addEventListener('pointerdown', () => { isDragging = false; });
  fb.addEventListener('pointermove', () => { isDragging = true; });
  
  fb.addEventListener('click', (e) => {
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
  });
'''

content = content.replace('  pf.loadFromHTML(pagesArray);', safe_click)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
