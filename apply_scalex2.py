# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the loadFromHTML part to wrap content
wrapper_logic = '''  allPages.forEach(page => {
    const inner = page.innerHTML;
    page.innerHTML = '<div style="transform: scaleX(-1); width: 100%; height: 100%;">' + inner + '</div>';
  });

  pf = new St.PageFlip(document.getElementById('flipBook'), {
    width:      w,
    height:     h,
    size:       'fixed',
    showCover:  true,
    usePortrait: window.innerWidth < 640,
    mobileScrollSupport: false,
    swipeDistance: 20,
    clickEventForward: true,
    drawShadow:  true,
    flippingTime: 650,
    maxShadowOpacity: 0.5,
  });

  pf.loadFromHTML(allPages);'''

content = re.sub(r'pf = new St\.PageFlip.*?pf\.loadFromHTML\(allPages\);', wrapper_logic, content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
