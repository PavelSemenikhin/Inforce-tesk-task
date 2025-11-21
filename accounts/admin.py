from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import Employee

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("user__username", "full_name", "position")
