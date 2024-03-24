from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home', views.home, name='home'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]