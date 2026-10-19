# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_openBook = '''function openBook() {
  document.getElementById('coverScreen').style.display = 'none';
  document.getElementById('bookScreen').style.display  = 'flex';
  document.getElementById('bookScreen').style.flexDirection = 'column';
  document.getElementById('bookScreen').style.alignItems = 'center';

  const { w, h } = bookSize();

  // Wrap all pages in scaleX(-1) to fix content mirroring
  allPages.forEach(page => {
    // Only wrap once (in case of double calls, though shouldn't happen)
    if (!page.dataset.wrapped) {
      const inner = page.innerHTML;
      page.innerHTML = '<div class="page-content" style="transform: scaleX(-1); width: 100%; height: 100%;">' + inner + '</div>';
      page.dataset.wrapped = "true";
    }
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

  pf.loadFromHTML(allPages);
}'''

# Replace from unction openBook() to pf.loadFromHTML(...);
content = re.sub(r'function openBook\(\) \{.*?pf\.loadFromHTML\([^\)]+\);\s*\}', new_openBook, content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
