from django.contrib.auth import get_user_model
from rest_framework import mixins, permissions, viewsets

from accounts.models import Employee
from accounts.serializers import (
    EmployeeCreateSerializer,
    EmployeeReadSerializer,
    RegisterSerializer,
)

User = get_user_model()


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoint for registering new users.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Endpoint for creating new employees.
    """

    queryset = Employee.objects.all()

    def get_permissions(self):
        if self.action in ["list", "retrieve", "update", "partial_update", "destroy"]:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Employee.objects.all()
        return Employee.objects.filter(user=user)

    def get_serializer_class(self):
        if self.action == "create":
            return EmployeeCreateSerializer
        return EmployeeReadSerializer
