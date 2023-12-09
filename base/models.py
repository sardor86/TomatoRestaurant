from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class MenuGroupModel(models.Model):
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        db_table = 'menu_group'
        verbose_name = 'Menu groups'
        verbose_name_plural = 'group'

    def __str__(self) -> str:
        return f'(Menu Group<{self.name}>)'

    def __repr__(self) -> str:
        return f'(Menu Group<{self.name}>)'


class MenuModel(models.Model):
    title = models.CharField('Name',
                             max_length=50)
    description = models.TextField('name',
                                   max_length=250)
    price = models.PositiveIntegerField('price($)')
    image = models.ImageField('image', upload_to='menu_images')
    specials = models.BooleanField('today special')
    group = models.ForeignKey(MenuGroupModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'menu'
        verbose_name = 'Meal'
        verbose_name_plural = 'Menu'

    def __str__(self) -> str:
        return f'(Menu<{self.title}>)'

    def __repr__(self) -> str:
        return f'(Menu<{self.title}>)'


class ReservationModel(models.Model):
    date_time = models.DateTimeField('date and time')
    name = models.CharField('client name',
                            max_length=50)
    email = models.EmailField('email')
    guest = models.PositiveSmallIntegerField('guests number')
    phone = models.PositiveBigIntegerField('phone number')

    class Meta:
        db_table = 'reservation'
        verbose_name = 'Client'
        verbose_name_plural = 'Orders'

    def __str__(self) -> str:
        return f'(Reservation<{self.name}>)'

    def __repr__(self) -> str:
        return f'(Reservation<{self.name}>)'


class TeamsModel(models.Model):
    name = models.CharField('name',
                            max_length=50)
    job_title = models.CharField('job title',
                                 max_length=50)
    image = models.ImageField(upload_to='team_images')

    class Meta:
        db_table = 'team'
        verbose_name = 'Team'
        verbose_name_plural = 'Your command'

    def __str__(self) -> str:
        return f'(Team<{self.name}>)'

    def __repr__(self) -> str:
        return f'(Team<{self.name}>)'


class GalleryModel(models.Model):
    image = models.ImageField(upload_to='gallery_images')

    class Meta:
        db_table = 'gallery'
        verbose_name = 'Picture'
        verbose_name_plural = 'Gallery'

    def __str__(self) -> str:
        return f'(Gallery<{self.image}>)'

    def __repr__(self) -> str:
        return f'(Gallery<{self.image}>)'


@receiver(pre_delete, sender=MenuModel)
def menu_photo_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(pre_delete, sender=TeamsModel)
def teams_photo_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(pre_delete, sender=GalleryModel)
def gallery_photo_delete(sender, instance, **kwargs):
    instance.image.delete(False)
