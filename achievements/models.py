from django.db import models


class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('admin',  'إدارية وتنظيمية'),
        ('tech',   'رقمية وتقنية'),
        ('social', 'اجتماعية وخدمية'),
    ]

    title       = models.CharField(max_length=300, verbose_name='العنوان')
    description = models.TextField(verbose_name='الوصف')
    date        = models.DateField(verbose_name='التاريخ')
    category    = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name='الفئة',
    )
    image       = models.ImageField(
        upload_to='achievements/',
        blank=True,
        null=True,
        verbose_name='الصورة',
    )
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')

    class Meta:
        verbose_name        = 'إنجاز'
        verbose_name_plural = 'الإنجازات'
        ordering            = ['-date']

    def __str__(self):
        return self.title

    def get_category_icon(self):
        icons = {'admin': '🏛️', 'tech': '💻', 'social': '🤝'}
        return icons.get(self.category, '⭐')

    def get_category_color(self):
        colors = {'admin': '#1a5276', 'tech': '#117a65', 'social': '#7d6608'}
        return colors.get(self.category, '#333')
