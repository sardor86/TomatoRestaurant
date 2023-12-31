from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from base.models import MenuModel


def shop_page(request: WSGIRequest):
    contex: dict = {'menu': MenuModel.objects.all().only('title', 'price', 'image')}
    return render(request,
                  'shop/templates/shop.html',
                  context=contex)
