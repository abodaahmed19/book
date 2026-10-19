# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_updateNav = '''function updateNav(page) {
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

content = re.sub(r'function updateNav.*?document\.getElementById\(\'btnNext\'\)\.onclick = \(\) => pf\.flipNext\(\);', new_updateNav, content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
