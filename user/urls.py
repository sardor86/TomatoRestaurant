from django.urls import path
from .views import register_login, register

urlpatterns = [
    path('', register_login, name='register-login'),
    path('api/user/register', register, name='register')
]
