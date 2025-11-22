from django.urls import include, path
from rest_framework.routers import DefaultRouter

from menus.views import MenuViewSet

app_name = "menus"

router = DefaultRouter()
router.register("", MenuViewSet, basename="menus")

urlpatterns = [
    path("", include(router.urls)),
]
