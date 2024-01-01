from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model

from base.models import MenuModel


User = get_user_model()


class Images(models.Model):
    meal = models.ForeignKey(MenuModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='meals_image')


class Rating(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(MenuModel, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
