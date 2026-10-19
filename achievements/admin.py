from django.contrib import admin
from .models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'date', 'created_at')
    list_filter   = ('category', 'date')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    ordering      = ('-date',)

    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('title', 'category', 'date'),
        }),
        ('التفاصيل', {
            'fields': ('description', 'image'),
        }),
    )
