# -*- coding: utf-8 -*-
import re
with open('templates/book.html', 'r', encoding='utf-8') as f:
    content = f.read()

media_queries = '''
@media (max-width: 900px) {
  #coverScreen { flex-direction: column; text-align: center; gap: 20px; }
  .intro-text { margin-bottom: 20px; text-align: center !important; }
}
@media (max-width: 600px) {
  .cover { width: 300px; min-height: 460px; }
  .spine { min-height: 460px; }
}
</style>'''

content = content.replace('</style>', media_queries)

with open('templates/book.html', 'w', encoding='utf-8') as f:
    f.write(content)
