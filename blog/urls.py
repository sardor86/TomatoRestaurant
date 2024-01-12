from django.urls import path
from .views import blog, blog_info


urlpatterns = [
    path('', blog, name='blog'),
    path('info/<int:blog_id>', blog_info, name='blog_info')
]
