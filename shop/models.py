from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model

from base.models import MenuModel


User = get_user_model()


class Images(models.Model):
    meal = models.ForeignKey(MenuModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='meals_image')

    class Meta:
        db_table = 'meal_images'
        verbose_name = 'image'
        verbose_name_plural = 'meal images'

    def __str__(self) -> str:
        return f'(MealImages<{self.meal}>)'

    def __repr__(self) -> str:
        return f'(MealImages<{self.meal}>)'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(MenuModel, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    date_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'rating'
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    def __str__(self) -> str:
        return f'(Rating<{self.user}:{self.meal}>)'

    def __repr__(self) -> str:
        return f'(Rating<{self.user}:{self.meal}>)'
