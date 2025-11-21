from django.db import models


class Restaurant(models.Model):

    class TypeChoice(models.TextChoices):
        UKRAINIAN = "UKRAINIAN"
        ASIAN = "ASIAN"
        ITALIAN = "ITALIAN"
        FAST_FOOD = "FAST_FOOD"
        OTHER = "OTHER"

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    type_of_food = models.CharField(
        choices=TypeChoice.choices,
        default=TypeChoice.OTHER,
        max_length=50,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        db_table = "restaurants"

    def __str__(self):
        return self.name
