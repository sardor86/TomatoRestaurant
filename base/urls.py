from django.urls import path
from .views import main_page, menu_page, reservation_page

urlpatterns = [
    path('', main_page, name='index'),
    path('menu', menu_page, name='menu'),
    path('reservation', reservation_page, name='reservation')
]
