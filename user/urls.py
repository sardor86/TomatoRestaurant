from django.urls import path
from .views import user_account, user_register, user_login

urlpatterns = [
    path('', user_account, name='account'),
    path('api/user/register', user_register, name='register'),
    path('api/user/login', user_login, name='login')
]
