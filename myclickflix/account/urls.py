from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')), 
    path('logout' , auth_views.LogoutView.as_view(), name = 'logout'),
    path('register/', views.register, name = 'register'), 
    path('edit/', views.edit, name='edit'), 
    path('', views.dashboard, name='dashboard'), 
]