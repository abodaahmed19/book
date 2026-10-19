# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

script_scale = '''
function scaleCover() {
  const vw = window.innerWidth, vh = window.innerHeight;
  const coverScreen = document.getElementById('coverScreen');
  if(!coverScreen) return;
  
  let s = 1;
  if (vw > 900) {
    s = Math.min(vw / 950, (vh - 40) / 650);
  } else {
    s = Math.min(vw / 450, (vh - 40) / 900);
  }
  
  if (s > 1.3) s = 1.3;
  if (s < 0.5) s = 0.5;
  
  coverScreen.style.transform = 'scale(' + s + ')';
  coverScreen.style.transformOrigin = 'center center';
}
'''
import re
content = re.sub(r'function scaleCover\(\) \{.*?\n\}', script_scale, content, flags=re.DOTALL)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
