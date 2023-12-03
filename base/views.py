from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def main_page(request: WSGIRequest):
    return render(
        request,
        'base/templates/index.html'
    )


def menu_page(request: WSGIRequest):
    return render(
        request,
        'base/templates/menu.html',
        context={
            'title': 'menu'
        }
    )


def reservation_page(request: WSGIRequest):
    return render(
        request,
        'base/templates/reservation.html',
        context={
            'title': 'reservation'
        }
    )


def about_page(request: WSGIRequest):
    return render(
        request,
        'base/templates/about.html',
        context={
            'title': 'about'
        }
    )


def gallery_page(request: WSGIRequest):
    return render(
        request,
        'base/templates/gallery.html',
        context={
            'title': 'gallery'
        }
    )
