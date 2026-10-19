# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove my array reverse hack
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

content = content.replace(old_rtl_logic, new_rtl_logic)

# 2. Add scaleX(-1) to flipBook and page
content = content.replace('#flipBook{', '#flipBook{\n  transform: scaleX(-1);')
content = content.replace('.page{', '.page{\n  transform: scaleX(-1);')

# 3. Fix updateNav
old_nav = '''function updateNav(page) {
  // In RTL, we reversed pages.
  // 0 is Back Cover, pagesArray.length - 1 is Front Cover
  const len = pf.getPageCount();
  // Arabic Next (flip left-to-right, which is pf.flipPrev) is disabled if we are at page 0
  document.getElementById('btnNext').disabled = page === 0;
  // Arabic Prev (flip right-to-left, which is pf.flipNext) is disabled if we are at last page
  document.getElementById('btnPrev').disabled = page >= len - 1;
  
  let label = '';
  if (page >= len - 1) label = 'الغلاف الأمامي';
  else if (page === 0) label = 'الغلاف الخلفي';
  else if (page === len - 2) label = 'مقدمة';
  else label = 'إنجاز ' + (len - 2 - page); // roughly
  
  document.getElementById('navInfo').textContent = label;
}

/* buttons */
// Arabic Next (left pointing) should trigger pf.flipPrev() which flips to the right revealing next Arabic page
document.getElementById('btnNext').onclick = () => pf.flipPrev();
// Arabic Prev (right pointing) should trigger pf.flipNext()
document.getElementById('btnPrev').onclick = () => pf.flipNext();
'''

new_nav = '''function updateNav(page) {
  document.getElementById('btnPrev').disabled = page === 0;
  document.getElementById('btnNext').disabled = page >= totalPgs - 1;
  document.getElementById('navInfo').textContent =
    page === 0            ? 'الغلاف الأمامي' :
    page >= totalPgs - 1  ? 'الغلاف الخلفي'  :
    page === 1            ? 'مقدمة' :
    page === 2            ? 'الفهرس' :
    'صفحة ' + (page - 2) + ' من ' + (totalPgs - 4);
}

/* buttons */
// Since we flipped the book with CSS scaleX(-1), pf.flipNext() (which normally flips right-to-left) 
// now visually flips left-to-right (which is Next in Arabic).
// So btnNext (left arrow) should trigger flipNext!
document.getElementById('btnNext').onclick = () => pf.flipNext();
document.getElementById('btnPrev').onclick = () => pf.flipPrev();
'''

if old_nav in content:
    content = content.replace(old_nav, new_nav)
else:
    # maybe some whitespace difference
    content = re.sub(r'function updateNav.*?document\.getElementById\(\'btnPrev\'\)\.onclick = \(\) => pf\.flipNext\(\);', new_nav, content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
