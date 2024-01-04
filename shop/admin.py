from django.contrib import admin

from .models import Images


@admin.register(Images)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['meal']
