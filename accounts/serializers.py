from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import Employee

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = ("id", "username", "password")
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "full_name", "position")
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = self.context["request"].user

        if hasattr(user, "employee"):
            raise serializers.ValidationError(
                {"detail": "Employee profile already exists for this user."}
            )

        return Employee.objects.create(user=user, **validated_data)


class EmployeeReadSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ("id", "user", "full_name", "position")
        read_only_fields = ("id",)
