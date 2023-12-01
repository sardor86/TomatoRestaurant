from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def main_page(request: WSGIRequest):
    return render(
        request,
        'base/templates/index.html'
    )
