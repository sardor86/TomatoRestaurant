from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from base.models import MenuModel, MenuGroupModel
from .forms import RatingForm
from .models import Images

from user.views import user_account


def shop_page(request: WSGIRequest):
    contex: dict = {
        'menu': MenuModel.objects.all().only('id', 'title', 'price', 'image'),
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


def meal_info_page(request: WSGIRequest, meal_id: int, error=None):
    contex: dict = {
        'meal': MenuModel.objects.filter(id=meal_id).only('id',
                                                          'title',
                                                          'price',
                                                          'image',
                                                          'description',
                                                          'full_description').first(),
        'images': Images.objects.filter(meal=meal_id),
        'error': error
    }

    return render(request,
                  'shop/templates/meal_detail.html',
                  context=contex)


def rating(request: WSGIRequest, meal_id):
    error = None
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RatingForm(request.POST)
            if form.is_valid():
                form.save(meal_id, request.user.id)
            else:
                error = 'invalid form'
        else:
            error = 'invalid form'
        return meal_info_page(request, meal_id, error)

    return user_account(request)
