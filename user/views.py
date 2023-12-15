from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def register_login(request: WSGIRequest):
    contex: dict = {
        'title': 'account'
    }
    return render(request,
                  'user/templates/shop_account.html',
                  contex)
