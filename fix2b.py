# -*- coding: utf-8 -*-
import re
with open('templates/admin_login.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<p class="text-muted small">.*?</p>', '<p class="text-muted small">للمسؤولين فقط</p>', content, count=1)
content = re.sub(r'>ÙƒÙ„Ù…Ø© Ø§Ù„Ù…Ø±ÙˆØ±<', '>كلمة المرور<', content)
content = re.sub(r'Ø£Ø¯Ø®Ù„ ÙƒÙ„Ù…Ø© Ø§Ù„Ù…Ø±ÙˆØ±', 'أدخل كلمة المرور', content)
content = re.sub(r'>Ø¯Ø®ÙˆÙ„<', '>دخول<', content)
content = re.sub(r'>Ø§Ù„Ø¹ÙˆØ¯Ø© Ù„Ù„Ø±Ø¦ÙŠØ³ÙŠØ©<', '>العودة للرئيسية<', content)

with open('templates/admin_login.html', 'w', encoding='utf-8') as f:
    f.write(content)
