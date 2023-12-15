from django.db import models


class UserModel(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
