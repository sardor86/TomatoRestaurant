from django.urls import path
from .views import main_page, menu_page, reservation_page, about_page, gallery_page

urlpatterns = [
    path('', main_page, name='index'),
    path('menu', menu_page, name='menu'),
    path('reservation', reservation_page, name='reservation'),
    path('about', about_page, name='about'),
    path('gallery', gallery_page, name='gallery'),
]
