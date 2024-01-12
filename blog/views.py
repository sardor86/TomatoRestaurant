from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from .models import Blog


def blog(request: WSGIRequest) -> HttpResponse:
    contex: dict = {
        'title': 'blog page',
        'blogs': Blog.objects.all()
    }
    return render(request,
                  'blog/templates/blog.html',
                  contex)


def blog_info(request: WSGIRequest, blog_id: int) -> HttpResponse:
    contex: dict = {
        'title': 'blog info',
        'blog': Blog.objects.filter(id=blog_id).first()
    }

    return render(request,
                  'blog/templates/blog_info.html',
                  contex)
