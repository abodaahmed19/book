# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update cover CSS
content = re.sub(
    r'\.cover\{.*?width:300px;min-height:480px;',
    '.cover{\n  width:400px;min-height:615px;',
    content, flags=re.DOTALL
)

# 2. Update spine CSS (needs to match new height)
content = re.sub(
    r'\.spine\{.*?min-height:480px;',
    '.spine{\n  min-height:615px;',
    content, flags=re.DOTALL
)

# 3. Insert intro-text into coverScreen
intro_html = '''
    <div class="intro-text" style="color: var(--cream); max-width: 400px; padding: 20px;">
      <h1 style="color: var(--gold); font-size: 3rem; margin-bottom: 20px; font-weight: 900;">سجل الإنجازات</h1>
      <p style="font-size: 1.3rem; line-height: 2; opacity: 0.9;">
        توثيق متكامل للجهود والمشاريع التي ساهمت في تطوير بيئة العمل والارتقاء بمستوى الخدمات. تصفح الكتاب لترى أثر الإنجاز.
      </p>
      <div style="margin-top: 30px; border-right: 4px solid var(--gold); padding-right: 15px; font-size: 1rem; opacity: 0.7;">
        «النجاح رحلة مستمرة، والإنجاز هو الوقود الذي يدفعنا للمزيد»
      </div>
    </div>
'''
content = content.replace('    <!-- spine -->', intro_html + '\n    <!-- spine -->')

# 4. Update coverScreen flex to have a gap
content = re.sub(
    r'#coverScreen\{.*?display:flex;align-items:center;',
    '#coverScreen{\n  position:relative;z-index:10;\n  display:flex;align-items:center;gap:50px;',
    content, flags=re.DOTALL
)

# 5. Update bookSize() function
new_bookSize = '''function bookSize() {
  const vw = window.innerWidth, vh = window.innerHeight;
  const maxW = Math.min(vw / 2.2, 550); 
  const maxH = Math.min(vh - 60, 800);
  
  let w = maxW;
  let h = w / 0.65;
  if (h > maxH) {
    h = maxH;
    w = h * 0.65;
  }
  return { w: Math.round(w), h: Math.round(h) };
}'''
content = re.sub(r'function bookSize\(\) \{.*?\n\}', new_bookSize, content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
