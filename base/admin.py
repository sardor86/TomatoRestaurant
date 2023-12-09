from django.contrib import admin
from base.models import MenuGroupModel, MenuModel, ReservationModel, TeamsModel, GalleryModel


@admin.register(MenuGroupModel)
class MenuGroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(MenuModel)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'specials')
    list_filter = ['specials']
    search_fields = ('title', 'price')


@admin.register(ReservationModel)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'name', 'guest', 'phone')
    search_fields = ('name', 'date_time', 'guest', 'phone')


@admin.register(TeamsModel)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title')
    search_fields = ('name', 'job_title')


@admin.register(GalleryModel)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']

