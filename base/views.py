from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from base.models import MenuModel, MenuGroupModel, TeamsModel, GalleryModel


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
    contex: dict = {
        'title': 'about',
        'group': TeamsModel.objects.all()
    }

    return render(
        request,
        'base/templates/about.html',
        contex
    )


def gallery_page(request: WSGIRequest):
    contex: dict = {
        'title': 'gallery',
        'gallery': GalleryModel.objects.all()
    }
    return render(
        request,
        'base/templates/gallery.html',
        contex
    )


def contact_page(request: WSGIRequest):
    contex: dict = {
        'title': 'contact'
    }

    return render(
        request,
        'base/templates/contact.html',
        contex
    )
