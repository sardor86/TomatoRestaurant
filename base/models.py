from django.db import models


class MenuModel(models.Model):
    title = models.CharField('Name',
                             max_length=50)
    description = models.TextField('name',
                                   max_length=250)
    price = models.PositiveIntegerField('price($)')
    image = models.ImageField('image')
    specials = models.BooleanField('today special')

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Menu'


class Reservation(models.Model):
    date_time = models.DateTimeField('date and time')
    name = models.CharField('client name',
                            max_length=50)
    email = models.EmailField('email')
    gest = models.PositiveSmallIntegerField('guests number')
    phone = models.PositiveBigIntegerField('phone number')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Orders'


class Teams(models.Model):
    name = models.CharField('name',
                            max_length=50)
    job_title = models.CharField('job title',
                                 max_length=50)
    image = models.ImageField()


class Gallery(models.Model):
    image = models.ImageField()
