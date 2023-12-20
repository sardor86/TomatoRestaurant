from django import forms
from django.contrib.auth.models import User
from user.models import UserModel

import os
import hashlib


class UserRegisterForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def check(self):
        data = self.cleaned_data
        if len(data['password1']) < 8:
            return 'password length is too short'

        if data['password1'] != data['password2']:
            return 'the passwords are not similar'

        return True

    def save(self):
        data = self.cleaned_data
        salt = os.urandom(32)
        password_hash = hashlib.pbkdf2_hmac('sha256',
                                            data['password1'].encode('utf-8'),
                                            salt,
                                            100000)
        user = UserModel(email=data['email'],
                         password=password_hash,
                         salt=salt)
        user.save()
