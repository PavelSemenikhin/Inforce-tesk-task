from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username


class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employee",
    )
    full_name = models.CharField(max_length=255)
    position = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "employees"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name
