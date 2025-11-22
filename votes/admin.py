from django.contrib import admin

from votes.models import Vote


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = (
        "employee__full_name",
        "menu__restaurant__name",
        "date",
    )
