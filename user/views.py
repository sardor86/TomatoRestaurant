from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .forms import UserRegisterForm, UserLoginForm


def register_login(request: WSGIRequest):
    contex: dict = {
        'title': 'account',
        'form': UserRegisterForm()
    }
    return render(request,
                  'user/templates/shop_account.html',
                  contex)


def register(request: WSGIRequest):
    contex: dict = {}

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form_check = form.check()
            if form_check is True:
                form.save()
                return render(request,
                              'user/templates/success.html',
                              contex)

            contex['register_error'] = form_check
        else:
            contex['register_error'] = 'form is invalid'

        return render(request,
                      'user/templates/shop_account.html',
                      contex)


def login(request: WSGIRequest):
    contex: dict = {}

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            form_check = form.check()
            if form_check is True:
                return render(request,
                              'user/templates/success.html',
                              contex)

            contex['login_error'] = form_check
        else:
            contex['login_error'] = 'form is invalid'

        return render(request,
                      'user/templates/shop_account.html',
                      contex)

