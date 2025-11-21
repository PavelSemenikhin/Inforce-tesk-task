import datetime

from django.db import models

from restaurants.models import Restaurant


class Menu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menus",
    )
    date = models.DateField(default=datetime.date.today)
    dishes = models.JSONField(default=dict)

    class Meta:
        ordering = ["-date"]
        db_table = "menus"
        constraints = [
            models.UniqueConstraint(
                fields=["restaurant", "date"],
                name="unique_restaurant_date",
            ),
        ]

    def __str__(self):
        return f"{self.restaurant.name} menu for {self.date}"
