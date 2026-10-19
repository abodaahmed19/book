# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Wrap spine and cover
content = content.replace('<!-- spine -->', '<div class="book-wrapper" style="display:flex; filter:drop-shadow(0 30px 60px rgba(0,0,0,.8));">\n    <!-- spine -->')
content = content.replace('</div><!-- #coverScreen -->', '</div>\n  </div><!-- #coverScreen -->')

# Remove drop-shadow from coverScreen to book-wrapper
content = content.replace('filter:drop-shadow(0 30px 60px rgba(0,0,0,.8));', '')

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
