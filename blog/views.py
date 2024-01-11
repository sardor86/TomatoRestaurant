from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def blog(request: WSGIRequest) -> HttpResponse:
    contex = {
        'title': 'blog page'
    }
    return render(request,
                  'blog/templates/blog.html',
                  contex)
