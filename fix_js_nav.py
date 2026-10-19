# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Fix openBook initialization of updateNav and buttons
new_openBook_tail = '''
  /* update nav */
  pf.on('flip', e => updateNav(e.data));
  pf.on('changeState', () => {});
  updateNav(startP);

  /* buttons */
  const btnNext = document.getElementById('btnNext');
  if(btnNext) btnNext.onclick = () => pf.flipPrev();
  const btnPrev = document.getElementById('btnPrev');
  if(btnPrev) btnPrev.onclick = () => pf.flipNext();
}'''

content = re.sub(r'/\* update nav \*/.*?document\.getElementById\(\'btnNext\'\)\.onclick = \(\) => pf\.flipNext\(\);\n\}', new_openBook_tail, content, flags=re.DOTALL)

# Fix updateNav function
new_updateNav = '''function updateNav(page) {
  const len = pf ? pf.getPageCount() : totalPgs;
  const btnNext = document.getElementById('btnNext');
  const btnPrev = document.getElementById('btnPrev');
  
  if (btnNext) btnNext.disabled = page === 0;
  if (btnPrev) btnPrev.disabled = page >= len - 1;
  
  let label = '';
  if (page >= len - 1) label = 'الغلاف الأمامي';
  else if (page === 0) label = 'الغلاف الخلفي';
  else if (page === len - 2) label = 'مقدمة';
  else label = 'إنجاز ' + (len - 2 - page); 
  
  const ni = document.getElementById('navInfo');
  if (ni) ni.textContent = label;
}'''

content = re.sub(r'function updateNav.*?\}', new_updateNav, content, flags=re.DOTALL, count=1)

# Fix keyboard events since closePage is gone, and arrow logic is reversed?
# ArrowRight normally means forward, ArrowLeft means backward.
# In Arabic, ArrowRight is NEXT (which goes left -> right, meaning flipPrev)
new_keyboard = '''/* keyboard */
document.addEventListener('keydown', e => {
  if (!pf) { if (e.key === 'Enter' || e.key === ' ') openBook(); return; }
  if (e.key === 'ArrowRight') pf.flipPrev();
  if (e.key === 'ArrowLeft')  pf.flipNext();
});'''

content = re.sub(r'/\* keyboard \*/.*?\n\}\);', new_keyboard, content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
