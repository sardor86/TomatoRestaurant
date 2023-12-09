from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from base.models import MenuModel, MenuGroupModel


def main_page(request: WSGIRequest):
    contex: dict = {
        'menu': MenuModel.objects.all(),
        'groups': MenuGroupModel.objects.all()
    }

    return render(
        request,
        'base/templates/index.html',
        contex
    )


def menu_page(request: WSGIRequest):
    contex: dict = {
        'title': 'menu',
        'menu': MenuModel.objects.all(),
        'groups': MenuGroupModel.objects.all()
    }

    return render(
        request,
        'base/templates/menu.html',
        contex
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
