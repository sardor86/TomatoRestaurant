from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import authenticate, login, get_user_model
from django.db.models import Q

from .forms import UserRegisterForm, UserLoginForm

User = get_user_model()


def user_account(request: WSGIRequest):
    contex: dict = {
        'title': 'account'
    }

    if request.user.is_authenticated:
        return render(request,
                      'user/templates/shop_account.html',
                      contex)
    return render(request,
                  'user/templates/login_register.html',
                  contex)


def user_register(request: WSGIRequest):
    contex: dict = {}

    if request.user.is_anonymous and request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user_data = form.cleaned_data
            email = user_data['email']
            username = user_data['username']
            check_email_username = User.objects.filter(Q(email=email) | Q(username=username)).first()
            if not check_email_username:
                password = user_data['password1']
                if password == user_data['password2'] and len(password) >= 8:
                    user = form.save(commit=False)
                    user.username = username
                    user.is_active = True
                    user.set_password(password)
                    user.save()

                    auth_user = authenticate(request, username=username, password=password)
                    login(request, auth_user)

                    return render(request,
                                  'user/templates/success.html')
                else:
                    contex['register_error'] = 'password is incorrect'
            else:
                contex['register_error'] = 'email is incorrect'
        else:
            contex['register_error'] = 'form is invalid'

        return render(request,
                      'user/templates/login_register.html',
                      contex,
                      status=400)


def user_login(request: WSGIRequest):
    contex: dict = {}

    if request.user.is_anonymous and request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user_data = form.cleaned_data

            username = user_data['username']
            password = user_data['password']

            check_email = User.objects.filter(username=username).first()

            if check_email:
                auth_user = authenticate(request, username=username, password=password)
                if auth_user:
                    login(request, auth_user)
                    return render(request,
                                  'user/templates/success.html',
                                  contex)
                else:
                    contex['login_error'] = 'password is incorrect'
            else:
                contex['login_error'] = 'email is not registered'
        else:
            contex['login_error'] = 'form is invalid'

        return render(request,
                      'user/templates/login_register.html',
                      contex,
                      status=400)

