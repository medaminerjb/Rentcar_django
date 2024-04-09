from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home', views.home, name='home'),
    path('voitures_listing',views.voitures_listing,name='voituresview'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]