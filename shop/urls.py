from django.urls import path
from .views import shop_page, shop_group_page, meal_info_page, rating


urlpatterns = [
    path('', shop_page, name='shop'),
    path('menu/group/<int:group_id>/', shop_group_page, name='shop_group'),
    path('meal/info/<int:meal_id>/', meal_info_page, name='meal_info'),
    path('rating/<int:meal_id>', rating, name='rating'),
]
