# -*- coding: utf-8 -*-
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove scaleX from .page
content = content.replace('.page{\n  transform: scaleX(-1);', '.page{')

# 2. Add .page-content wrapper CSS
content = content.replace('.page{', '.page-content {\n  transform: scaleX(-1);\n  width: 100%;\n  height: 100%;\n}\n.page{')

# 3. Wrap inner content of every .page in <div class="page-content">
import re
def wrap_page(match):
    inner = match.group(2)
    return match.group(1) + '\n<div class="page-content">\n' + inner + '\n</div>\n</div>'

# We match <div class="page ..."> ... </div>
# Wait, parsing HTML with regex is hard. Let's just do it simply.
# We know pages are:
# <div class="page page-cover" data-density="hard">
# <div class="pc-inner">...</div>
# </div>
# So we can replace <div class="pc-inner"> with <div class="page-content"><div class="pc-inner">
# and </div>\n      </div> with </div></div>\n      </div> for the covers.
# For .page-inner, we have <div class="pg-head"> ... <div class="pg-num">...</div>
# It's better to just write a short python script that uses BeautifulSoup, or since it's Django template, we can just replace the start and end of the page.

# Actually, my array reverse logic worked PERFECTLY, except it was a bit complex.
# The user already tested it? No, the user saw my first patch which used stretch. The user never saw my array reverse logic!
