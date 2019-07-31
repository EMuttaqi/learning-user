from django.urls import path
## for django 1 import re_path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
#####
    path('activate/<str:uidb64>/<str:token>',
        views.activate, name='activate'),
#####
]
