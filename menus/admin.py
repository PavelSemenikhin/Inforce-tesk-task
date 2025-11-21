from django.contrib import admin

from menus.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("restaurant__name", "date", "dishes")
