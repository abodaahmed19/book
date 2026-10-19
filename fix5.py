# -*- coding: utf-8 -*-
with open('templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Ø¬Ù…ÙŠØ¹ Ø§Ù„Ø­Ù‚ÙˆÙ‚ Ù…Ø­Ù ÙˆØ¸Ø©', 'جميع الحقوق محفوظة')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('templates/admin_login.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Ø£Ø¯Ø®Ù„ اسم المستخدم', 'أدخل اسم المستخدم')
content = content.replace('Ø£Ø¯Ø®Ù„ كلمة المرور', 'أدخل كلمة المرور')

with open('templates/admin_login.html', 'w', encoding='utf-8') as f:
    f.write(content)
