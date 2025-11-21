from rest_framework import serializers

from restaurants.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = (
            "id",
            "name",
            "description",
            "type_of_food",
            "created_at",
        )
        read_only_fields = ("id", "created_at")
