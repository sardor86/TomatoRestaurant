from django.urls import path
from .views import shop_page


urlpatterns = [
    path('', shop_page, name='shop')
]
