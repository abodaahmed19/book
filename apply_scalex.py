# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove my array reverse hack from openBook
old_rtl_logic = '''  let pagesArray = Array.from(allPages);
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

  pf.loadFromHTML(pagesArray);'''

new_rtl_logic = '''  pf = new St.PageFlip(document.getElementById('flipBook'), {
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

if old_rtl_logic in content:
    content = content.replace(old_rtl_logic, new_rtl_logic)
else:
    # use regex just in case
    content = re.sub(r'let pagesArray = Array\.from\(allPages\);.*?pf\.loadFromHTML\(pagesArray\);', new_rtl_logic, content, flags=re.DOTALL)


# 2. Add scaleX(-1) to flipBook
content = content.replace('#flipBook{', '#flipBook{\n  transform: scaleX(-1);')

# 3. Add a page-content wrapper to all pages to flip content back
def wrap_page(m):
    # m.group(1) is the opening div of .page
    # m.group(2) is the inner HTML
    return m.group(1) + '\n<div class="page-wrapper" style="transform: scaleX(-1); width: 100%; height: 100%;">' + m.group(2) + '</div>\n</div>'

# Actually it's easier to just do it via DOM in JS before loadFromHTML!
# Let's inject JS to wrap the innerHTML of every page in a scaleX(-1) div!
