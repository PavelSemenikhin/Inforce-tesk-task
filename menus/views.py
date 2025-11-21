from datetime import date

from rest_framework import viewsets, permissions

from menus.models import Menu
from menus.serializers import MenuReadSerializer, MenuCreateSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    Endpoints for  Menu with dishes like JSON field.
    """

    def get_queryset(self):
        if self.action == "list":
            return Menu.objects.filter(date=date.today())
        return Menu.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MenuReadSerializer
        return MenuCreateSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
