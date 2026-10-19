from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('',      views.book,   name='book'),

    # Admin Panel
    path('ctrl/login/',   views.admin_login,   name='admin_login'),
    path('ctrl/logout/',  views.admin_logout,  name='admin_logout'),
    path('ctrl/',         views.dashboard,     name='dashboard'),
    path('ctrl/add/',     views.achievement_add,    name='achievement_add'),
    path('ctrl/edit/<int:pk>/',   views.achievement_edit,   name='achievement_edit'),
    path('ctrl/delete/<int:pk>/', views.achievement_delete, name='achievement_delete'),
]
