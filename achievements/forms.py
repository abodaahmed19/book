from django import forms
from .models import Achievement


class AchievementForm(forms.ModelForm):
    class Meta:
        model  = Achievement
        fields = ['title', 'description', 'date', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل عنوان الإنجاز',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'أدخل وصف تفصيلي للإنجاز',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
        }
        labels = {
            'title':       'العنوان',
            'description': 'الوصف',
            'date':        'التاريخ',
            'category':    'الفئة',
            'image':       'الصورة (اختياري)',
        }
