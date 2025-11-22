from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/accounts/",
        include("accounts.urls"),
        name="accounts",
    ),
    path(
        "api/restaurants/",
        include("restaurants.urls"),
        name="restaurants",
    ),
    path(
        "api/menus/",
        include("menus.urls"),
        name="menus",
    ),
    path(
        "api/votes/",
        include("votes.urls"),
        name="votes",
    ),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
]
