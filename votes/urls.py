from django.urls import path, include
from rest_framework.routers import DefaultRouter

from votes.views import VoteViewSet, VoteResultApiView, WinnerApiView

app_name = "votes"

router = DefaultRouter()
router.register("votes", VoteViewSet, basename="votes")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "results/",
        VoteResultApiView.as_view(),
        name="results",
    ),
    path(
        "todays_winner/",
        WinnerApiView.as_view(),
        name="today_winner",
    ),
]
