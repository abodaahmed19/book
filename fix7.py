# -*- coding: utf-8 -*-
import re
with open('achievements/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'ØªÙ… Ø¥Ø¶Ø§Ù Ù© Ø§Ù„Ø¥Ù†Ø¬Ø§Ø² Ø¨Ù†Ø¬Ø§Ø­ âœ…', 'تم إضافة الإنجاز بنجاح ✅', content)
content = re.sub(r'ØªÙ… Ø¥Ø¶Ø§Ù Ù© Ø§Ù„Ø¥Ù†Ø¬Ø§Ø²', 'تم إضافة الإنجاز', content)
content = re.sub(r'ØªÙ… Ø­Ø°Ù  Ø§Ù„Ø¥Ù†Ø¬Ø§Ø² Ø¨Ù†Ø¬Ø§Ø­', 'تم حذف الإنجاز بنجاح', content)
content = re.sub(r'Ø¥Ø¶Ø§Ù Ù©', 'إضافة', content)
content = re.sub(r'ØªØ¹Ø¯ÙŠÙ„', 'تعديل', content)

# just hardcode replacing the known lines if regex fails
lines = content.split('\n')
for i, l in enumerate(lines):
    if 'messages.success' in l and 'âœ…' in l:
        lines[i] = "            messages.success(request, 'تم إضافة/تعديل الإنجاز بنجاح ✅')"
    if 'messages.success' in l and 'ØªÙ… Ø­Ø°Ù ' in l:
        lines[i] = "        messages.success(request, 'تم حذف الإنجاز بنجاح')"
    if 'action' in l and 'Ø¥Ø¶Ø§Ù Ù©' in l:
        lines[i] = "    return render(request, 'achievement_form.html', {'form': form, 'action': 'إضافة'})"

content = '\n'.join(lines)
with open('achievements/views.py', 'w', encoding='utf-8') as f:
    f.write(content)
