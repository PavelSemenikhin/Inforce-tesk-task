from rest_framework import serializers

from menus.models import Menu
from votes import services
from votes.models import Vote


class VoteCreateSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Menu.objects.all()
    )

    class Meta:
        model = Vote
        fields = (
            "id",
            "menu",
        )
        read_only_fields = ("id", "date")

    def create(self, validated_data):
        user = self.context["request"].user
        menu = validated_data.pop("menu")
        return services.create_vote_for_user(user, menu)


class VoteReadSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(read_only=True)
    menu = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Vote
        fields = ("id", "employee", "menu", "date")
        read_only_fields = ("id", "date")
