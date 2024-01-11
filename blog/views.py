from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from .models import Blog


def blog(request: WSGIRequest) -> HttpResponse:
    contex = {
        'title': 'blog page',
        'blogs': Blog.objects.all()
    }
    return render(request,
                  'blog/templates/blog.html',
                  contex)
