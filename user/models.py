from django.db import models


class UserModel(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.BinaryField(max_length=50)
    salt = models.BinaryField(max_length=32)

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'
