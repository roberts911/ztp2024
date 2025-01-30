# filepath: /home/rsiurek/szu/accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('apply/', views.apply, name='apply'),
    path('status/', views.status, name='status'),
    path('approve/<str:nip>/', views.approve, name='approve'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api_key/', views.api_key, name='api_key'),
]