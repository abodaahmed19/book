# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove buttons
content = re.sub(r'<!-- Fixed UI buttons -->.*?<!-- Messages -->', '<!-- Messages -->', content, flags=re.DOTALL)
# Also remove updateNav function since nav buttons are gone? Or leave it, it's harmless.
# Actually, the user asked to remove them.

# 2. Fix border-radius for spine and cover
content = re.sub(r'border-radius:6px 0 0 6px;', 'border-radius:0 6px 6px 0;', content)
content = re.sub(r'border-radius:0 4px 4px 0;', 'border-radius:4px 0 0 4px;', content)

# 3. Fix size: stretch back to fixed
content = content.replace("size:       'stretch',", "size:       'fixed',")

# 4. Remove width/height 100vw from flipBook
content = re.sub(r'#flipBook\{\s*width: 100vw;\s*height: 100vh;', '#flipBook{', content, flags=re.DOTALL)

# 5. Inject RTL logic into openBook
rtl_logic = '''  let pagesArray = Array.from(allPages);
  if (pagesArray.length % 2 !== 0) {
    let blank = document.createElement('div');
    blank.className = 'page page-inner';
    blank.innerHTML = '<div class="pg-head"></div><div style="display:flex;height:100%;align-items:center;justify-content:center;opacity:0.3;font-size:2rem;"><i class="fas fa-leaf"></i></div>';
    let backCover = pagesArray.pop();
    pagesArray.push(blank);
    pagesArray.push(backCover);
  }
  pagesArray.reverse();
  const startP = pagesArray.length - 1;

  pf = new St.PageFlip(document.getElementById('flipBook'), {
    width:      w,
    height:     h,
    size:       'fixed',
    showCover:  true,
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
'''
content = re.sub(r'pf = new St\.PageFlip.*?pf\.loadFromHTML\(allPages\);', rtl_logic, content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
