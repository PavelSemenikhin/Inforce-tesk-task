from django.urls import include, path
from rest_framework.routers import DefaultRouter

from restaurants.views import RestaurantViewSet

app_name = "restaurants"

router = DefaultRouter()
router.register("", RestaurantViewSet, basename="restaurants")

urlpatterns = [
    path("", include(router.urls)),
]
