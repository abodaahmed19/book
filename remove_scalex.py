# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Remove scaleX(-1) from CSS
content = content.replace('transform: scaleX(-1);', '')

# Update openBook JS
new_js = '''function openBook() {
  document.getElementById('coverScreen').style.display = 'none';
  document.getElementById('bookScreen').style.display  = 'flex';
  document.getElementById('bookScreen').style.flexDirection = 'column';
  document.getElementById('bookScreen').style.alignItems = 'center';

  const { w, h } = bookSize();

  let pagesArray = Array.from(allPages);
  
  // Clean up any previously injected page-content wrappers just in case
  pagesArray.forEach(page => {
    if (page.dataset.wrapped) {
      page.innerHTML = page.querySelector('.page-content').innerHTML;
      page.dataset.wrapped = "";
    }
  });

  // Ensure EVEN number of pages
  if (pagesArray.length % 2 !== 0) {
    let blank = document.createElement('div');
    blank.className = 'page page-inner';
    blank.innerHTML = '<div class="pg-head"></div><div style="display:flex;height:100%;align-items:center;justify-content:center;opacity:0.3;font-size:2rem;"><i class="fas fa-leaf"></i></div>';
    pagesArray.push(blank);
  }

  // Reverse array for RTL reading order
  pagesArray.reverse();
  
  // startPage must be EVEN when showCover is false
  const startP = pagesArray.length - 2;

  pf = new St.PageFlip(document.getElementById('flipBook'), {
    width:      w,
    height:     h,
    size:       'fixed',
    showCover:  false,
    startPage:  startP,
    usePortrait: window.innerWidth < 640,
    mobileScrollSupport: false,
    swipeDistance: 20,
    clickEventForward: true,
    drawShadow:  true,
    flippingTime: 650,
    maxShadowOpacity: 0.5,
  });

  pf.loadFromHTML(pagesArray);
}'''

content = re.sub(r'function openBook\(\) \{.*?pf\.loadFromHTML\([^\)]+\);\s*\}', new_js, content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
