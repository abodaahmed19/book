# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('function openBook() {')
if start_idx != -1:
    end_idx = content.find('/* fullscreen */', start_idx)
    
    new_js = '''function openBook() {
  document.getElementById('coverScreen').style.display = 'none';
  document.getElementById('bookScreen').style.display  = 'flex';
  document.getElementById('bookScreen').style.flexDirection = 'column';
  document.getElementById('bookScreen').style.alignItems = 'center';

  const { w, h } = bookSize();

  // Wrap all pages in scaleX(-1) to fix content mirroring
  allPages.forEach(page => {
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
}

'''
    
    content = content[:start_idx] + new_js + content[end_idx:]
    
with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
