from django.contrib import admin

from restaurants.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "type_of_food",
        "created_at",
    )
