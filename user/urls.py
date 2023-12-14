from django.urls import path
from .views import register_login

urlpatterns = [
    path('', register_login, name='register-login')
]
