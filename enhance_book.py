# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the cover pages
# Front Cover
content = re.sub(r'<!-- PAGE 0: Front Cover \(hard\) -->.*?</div>\s*</div>\s*<!-- PAGE 1: Intro', '<!-- PAGE 1: Intro', content, flags=re.DOTALL)
# Back Cover
content = re.sub(r'<!-- BACK COVER \(hard\) -->.*?</div>\s*</div>\s*</div><!-- #flipBook -->', '</div><!-- #flipBook -->', content, flags=re.DOTALL)

# 2. Update showCover: true to showCover: false
content = content.replace('showCover:  true,', 'showCover:  false,')

# 3. Enhance CSS for .page and .page-inner
new_page_css = '''
.page{
  background: linear-gradient(180deg, #fdfaf3 0%, #f6f0df 100%);
  font-family:'Cairo',sans-serif;
  overflow:hidden;
  position:relative;
  box-shadow: inset 0 0 20px rgba(0,0,0,0.05);
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 4px;
}
.page::before {
  content: "";
  position: absolute;
  top: 0; bottom: 0; left: 0; right: 0;
  box-shadow: inset 0 0 10px rgba(201,162,39,0.1);
  pointer-events: none;
}
.page-inner{
  padding:25px 25px 20px;
  display:flex;flex-direction:column;
  height: 100%;
}
'''

content = re.sub(r'\.page\{.*?\}\s*\.page-inner\{.*?\}', new_page_css, content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
