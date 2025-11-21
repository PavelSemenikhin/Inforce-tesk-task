from datetime import date

from rest_framework import serializers

from menus.models import Menu
from restaurants.models import Restaurant


class MenuCreateSerializer(serializers.ModelSerializer):

    restaurant = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Restaurant.objects.all(),
    )
    dishes = serializers.JSONField(
        help_text="JSON object with dishes for this menu.",
    )

    class Meta:
        model = Menu
        fields = ("id", "restaurant", "date", "dishes")
        read_only_fields = ("id", "date")

    def validate(self, attrs):
        restaurant = attrs["restaurant"]
        today = date.today()

        if Menu.objects.filter(restaurant=restaurant, date=today).exists():
            raise serializers.ValidationError(
                {"detail": "Menu for this restaurant already exists for today."}
            )
        return attrs


class MenuReadSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Menu
        fields = ("id", "restaurant", "date", "dishes")
        read_only_fields = ("id", "date")
