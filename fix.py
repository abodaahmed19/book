# -*- coding: utf-8 -*-
with open('templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'ÙƒØªØ§Ø¨ Ø§Ù„Ø¥Ù†Ø¬Ø§Ø²Ø§Øª Ø§Ù„Ø¥Ø¯Ø§Ø±ÙŠØ©': 'كتاب الإنجازات الإدارية',
    'Ø§Ù„ÙƒØªØ§Ø¨': 'الكتاب',
    'Ù„ÙˆØ­Ø© Ø§Ù„ØªØ­ÙƒÙ…': 'لوحة التحكم',
    'Ø®Ø±ÙˆØ¬': 'خروج',
    'Ø¯Ø®ÙˆÙ„ Ø§Ù„Ø¥Ø¯Ø§Ø±Ø©': 'دخول الإدارة',
    'Ø¬Ù…ÙŠØ¹ Ø§Ù„Ø­Ù‚ÙˆÙ‚ Ù…Ø­Ù ÙˆØ¸Ø©': 'جميع الحقوق محفوظة'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)
