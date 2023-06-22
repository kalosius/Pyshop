from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('garages/', views.garages, name='garage'),
    path('mechanics/', views.mechanics, name='mechanics'),
    path('vehicles/', views.vehicles, name='vehicles'),
    
]