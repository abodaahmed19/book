# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Disable clickEventForward
content = content.replace('clickEventForward: true,', 'clickEventForward: false,')

# Add custom click listener after loadFromHTML
custom_click = '''  pf.loadFromHTML(pagesArray);

  // Custom click logic to satisfy LTR digital expectations for RTL reading
  document.getElementById('flipBook').addEventListener('click', (e) => {
    // Only handle clicks, not drags. 
    // Wait, how do we distinguish click from drag? 
    // pageFlip prevents default or stops propagation on drag?
    // Actually, pageFlip might swallow the click event if it was a drag!
    // But to be safe, we can just use a simple click listener.
    const rect = e.currentTarget.getBoundingClientRect();
    const x = e.clientX - rect.left;
    
    // Check if it's in the corners for flipping (e.g. standard click zones)
    // PageFlip's default click zone is usually the entire page or a margin.
    // Let's just use the whole half.
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

content = re.sub(r'pf\.loadFromHTML\(pagesArray\);', custom_click, content)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
