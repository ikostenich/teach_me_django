from django.contrib import admin
from django.db import models

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
