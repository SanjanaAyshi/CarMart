from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='userLogin'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.editProfile, name='editProfile'),
    path('profile/edit/passChange/', views.passChange, name='passChange'),
    path('logout/', views.LogoutView.as_view(), name='userLogout'),
]
