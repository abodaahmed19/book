# -*- coding: utf-8 -*-
with open('achievements/views.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
lines[73] = "    return render(request, 'achievement_form.html', {'form': form, 'action': 'إضافة'})\n"
lines[95] = "        messages.success(request, 'تم حذف الإنجاز بنجاح')\n"
with open('achievements/views.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
