from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count, Q
from .models import Achievement
from .forms import AchievementForm


# â”€â”€â”€ Public Views â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def book(request):
    achievements = Achievement.objects.all()
    total        = achievements.count()
    admin_count  = achievements.filter(category='admin').count()
    tech_count   = achievements.filter(category='tech').count()
    social_count = achievements.filter(category='social').count()

    return render(request, 'book.html', {
        'achievements': achievements,
        'total':        total,
        'admin_count':  admin_count,
        'tech_count':   tech_count,
        'social_count': social_count,
        'categories':   Achievement.CATEGORY_CHOICES,
    })


# â”€â”€â”€ Admin Panel Views â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    return render(request, 'admin_login.html')


def admin_logout(request):
    logout(request)
    return redirect('book')


@login_required
def dashboard(request):
    achievements = Achievement.objects.all()
    stats = {
        'total':  achievements.count(),
        'admin':  achievements.filter(category='admin').count(),
        'tech':   achievements.filter(category='tech').count(),
        'social': achievements.filter(category='social').count(),
    }
    return render(request, 'dashboard.html', {
        'achievements': achievements,
        'stats':        stats,
    })


@login_required
def achievement_add(request):
    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة/تعديل الإنجاز بنجاح ✅')
            return redirect('dashboard')
    else:
        form = AchievementForm()
    return render(request, 'achievement_form.html', {'form': form, 'action': 'إضافة'})


@login_required
def achievement_edit(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES, instance=achievement)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل الإنجاز بنجاح ✅')
            return redirect('dashboard')
    else:
        form = AchievementForm(instance=achievement)
    return render(request, 'achievement_form.html', {'form': form, 'action': 'تعديل', 'obj': achievement})


@login_required
def achievement_delete(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        achievement.delete()
        messages.success(request, 'تم حذف الإنجاز بنجاح')
        return redirect('dashboard')
    return render(request, 'achievement_confirm_delete.html', {'achievement': achievement})

