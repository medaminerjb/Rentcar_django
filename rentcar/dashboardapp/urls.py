from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('caradd', views.addcar, name='caradd'),
    path('rentcar', views.addcar, name='caradd'),
    path('delete/<int:id>/',views.deletecar,name='delete'),
    path('get_edit/<int:id>/',views.getcar,name='get_edit')

]
