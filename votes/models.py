from django.db import models
from django.db.models import UniqueConstraint

from accounts.models import Employee
from menus.models import Menu


class Vote(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="votes",
    )
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="votes")
    date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["employee", "date"],
                name="unique_employee_date",
            ),
        ]
        db_table = "votes"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.employee.full_name}-{self.menu.restaurant.name}-{self.date}."
