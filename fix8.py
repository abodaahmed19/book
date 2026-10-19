# -*- coding: utf-8 -*-
with open('achievements/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('ØªÙ… Ø­Ø°Ù  Ø§Ù„Ø¥Ù†Ø¬Ø§Ø² Ø¨Ù†Ø¬Ø§Ø­', 'تم حذف الإنجاز بنجاح')
content = content.replace('Ø¥Ø¶Ø§Ù Ø©', 'إضافة')

with open('achievements/views.py', 'w', encoding='utf-8') as f:
    f.write(content)
