# users/urls.py
from django.urls import path
from .views import register, user_login, clienteView
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('client/', clienteView, name='clienteView'),
    path('index', views.index, name='index'), 
]

