from django.urls import path, include
from rest_framework.routers import DefaultRouter

from menus.views import MenuViewSet


app_name = "menus"

router = DefaultRouter()
router.register("menus", MenuViewSet, basename="menus")

urlpatterns = [
    path("", include(router.urls)),
]
