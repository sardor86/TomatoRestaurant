from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
