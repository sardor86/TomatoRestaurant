from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from .models import Blog, BlogComment
from .forms import BlogCommentForm

from user.views import user_account


def blog(request: WSGIRequest) -> HttpResponse:
    contex: dict = {
        'title': 'blog page',
        'blogs': Blog.objects.all()
    }
    return render(request,
                  'blog/templates/blog.html',
                  contex)


def blog_info(request: WSGIRequest, blog_id: int, status: int = None) -> HttpResponse:
    contex: dict = {
        'title': 'blog info',
        'blog': Blog.objects.filter(id=blog_id).first(),
        'comments': BlogComment.objects.filter(blog=blog_id).all()
    }

    return render(request,
                  'blog/templates/blog_info.html',
                  contex,
                  status=status)


def blog_comment(request: WSGIRequest, blog_id: int) -> HttpResponse:
    if request.method == "POST":
        if request.user.is_authenticated:
            form = BlogCommentForm(request.POST)

            if form.is_valid():
                form.save(blog_id, request.user.id)
                return blog_info(request, blog_id)
        else:
            return user_account(request)
    return blog_info(request, blog_id, status=400)
