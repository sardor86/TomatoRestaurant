from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from base.models import MenuModel, MenuGroupModel
from .models import Images, Rating


def shop_page(request: WSGIRequest):
    contex: dict = {
        'menu': MenuModel.objects.all().only('id','title', 'price', 'image'),
        'groups': MenuGroupModel.objects.all()
    }
    return render(request,
                  'shop/templates/shop.html',
                  context=contex)


def shop_group_page(request: WSGIRequest, group_id: int):
    contex: dict = {
        'menu': MenuModel.objects.filter(group=group_id).all().only('id', 'title', 'price', 'image'),
        'groups': MenuGroupModel.objects.all()
    }
    return render(request,
                  'shop/templates/shop.html',
                  context=contex)


def meal_info_page(request: WSGIRequest, meal_id: int):
    contex: dict = {
        'meal': MenuModel.objects.filter(id=meal_id).only('title',
                                                          'price',
                                                          'image',
                                                          'description',
                                                          'full_description').first(),
        'images': Images.objects.filter(meal=meal_id)
    }

    return render(request,
                  'shop/templates/meal_detail.html',
                  context=contex)
