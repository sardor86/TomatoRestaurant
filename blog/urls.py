from django.urls import path
from .views import blog, blog_info, blog_comment


urlpatterns = [
    path('', blog, name='blog'),
    path('info/<int:blog_id>', blog_info, name='blog_info'),
    path('comment/<int:blog_id>', blog_comment, name='blog_comment')
]
