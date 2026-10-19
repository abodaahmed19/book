# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

script_scale = '''
function scaleCover() {
  const vw = window.innerWidth, vh = window.innerHeight;
  // Wrapper is around 900px wide and 650px high
  let s = Math.min(vw / 950, (vh - 40) / 650);
  if (s > 1.5) s = 1.5; // limit max scale
  const coverScreen = document.getElementById('coverScreen');
  if(coverScreen) {
    coverScreen.style.transform = 'scale(' + s + ')';
    coverScreen.style.transformOrigin = 'center center';
  }
}
window.addEventListener('resize', scaleCover);
document.addEventListener('DOMContentLoaded', scaleCover);
'''

if 'function scaleCover()' not in content:
    content = content.replace('</script>', script_scale + '\n</script>')

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
