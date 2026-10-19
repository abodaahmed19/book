# -*- coding: utf-8 -*-
import re
with open('templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'Ø¬Ù…ÙŠØ¹ Ø§Ù„Ø­Ù‚ÙˆÙ‚ Ù…Ø­Ù ÙˆØ¸Ø©', 'جميع الحقوق محفوظة', content)
content = re.sub(r'<p class="mb-0 small opacity-75">.*?&copy;', '<p class="mb-0 small opacity-75">جميع الحقوق محفوظة &copy;', content)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)
