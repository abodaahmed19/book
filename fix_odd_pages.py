# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

new_js = '''  let pagesArray = Array.from(allPages);
  if (pagesArray.length % 2 !== 0) {
    let blank = document.createElement('div');
    blank.className = 'page page-inner';
    blank.innerHTML = '<div class="pg-head"></div><div style="display:flex;height:100%;align-items:center;justify-content:center;opacity:0.3;font-size:2rem;"><i class="fas fa-leaf"></i></div>';
    let backCover = pagesArray.pop();
    pagesArray.push(blank);
    pagesArray.push(backCover);
  }

  // Wrap all pages in scaleX(-1) to fix content mirroring
  pagesArray.forEach(page => {
    if (!page.dataset.wrapped) {
      const inner = page.innerHTML;
      page.innerHTML = '<div class="page-content" style="transform: scaleX(-1); width: 100%; height: 100%;">' + inner + '</div>';
      page.dataset.wrapped = "true";
    }
  });

  pf = new St.PageFlip(document.getElementById('flipBook'), {'''

content = content.replace('''  // Wrap all pages in scaleX(-1) to fix content mirroring
  allPages.forEach(page => {
    if (!page.dataset.wrapped) {
      const inner = page.innerHTML;
      page.innerHTML = '<div class="page-content" style="transform: scaleX(-1); width: 100%; height: 100%;">' + inner + '</div>';
      page.dataset.wrapped = "true";
    }
  });

  pf = new St.PageFlip(document.getElementById('flipBook'), {''', new_js)

content = content.replace('pf.loadFromHTML(allPages);', 'pf.loadFromHTML(pagesArray);')

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
