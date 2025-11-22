from datetime import date

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from menus.models import Menu
from menus.serializers import MenuCreateSerializer, MenuReadSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    Endpoints for  Menu with dishes like JSON field.
    """

    def list(self, request, *args, **kwargs):
        version = request.app_version

        if version == "1.0":
            return Response({"menus": super().list(request).data})

        return super().list(request)

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
