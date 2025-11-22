from datetime import date

from django.db.models.aggregates import Count
from rest_framework import serializers

from menus.models import Menu
from votes.models import Vote


def create_vote_for_user(user, menu):
    """
    Validates voting rules and creates a new Vote instance for the given user.
    Raises serializers.ValidationError on invalid action.
    """
    today = date.today()

    if not hasattr(user, "employee"):
        raise serializers.ValidationError(
            {"detail": "Employee profile does not exist for this user."}
        )
    if menu.date != today:
        raise serializers.ValidationError(
            {"detail": "You can vote only for today`s menu."}
        )
    if Vote.objects.filter(employee=user.employee, date=today).exists():

        raise serializers.ValidationError(
            {"detail": "You already voted today."},
        )
    return Vote.objects.create(employee=user.employee, menu=menu)


def get_vote_result():
    today = date.today()

    results = (
        Menu.objects.filter(date=today)
        .annotate(votes_count=Count("votes"))
        .values(
            "id",
            "restaurant__name",
            "date",
            "votes_count",
        )
    )
    return results

def get_today_winner():
    today = date.today()

    winner = (
        (Menu.objects.filter(date=today))
        .annotate(votes_count=Count("votes"))
        .order_by("-votes_count")
        .values(
            "id",
            "restaurant__name",
            "dishes",
            "date",
            "votes_count",
        )
        .first()
    )

    if not winner or winner["votes_count"] == 0:
        return None
    return winner
