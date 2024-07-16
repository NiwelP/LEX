from django.urls import path
from .views import register, user_login, user_logout, profile, create_request, admin_requests_view, index
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('create-request/', create_request, name='create_request'),
    path('admin-requests/', admin_requests_view, name='admin_requests'),
    path('index/', index, name= 'index')
]