from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.index, name = 'index'),
    path('home/', views.index, name = 'home'),
    path('loginpage/', auth_views.LoginView.as_view(template_name = 'loginpage.html'), name = 'login' ),
    path('logoutpage/', auth_views.LogoutView.as_view(template_name = 'logoutpage.html'), name = 'logoutpage' ),
    
    # path('', views.index, name='views'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    # path('login', views.login, name='login'),
    
    path('services/', views.services, name='services'),
    path('data/', views.data, name='data')
    

]