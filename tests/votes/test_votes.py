import pytest
from rest_framework.test import APIClient
from django.utils import timezone

from django.contrib.auth import get_user_model
from restaurants.models import Restaurant
from menus.models import Menu
from accounts.models import Employee
from votes.models import Vote

User = get_user_model()


@pytest.mark.django_db
def test_vote_success():
    client = APIClient()

    user = User.objects.create_user(username="u1", password="pass12345")
    emp = Employee.objects.create(user=user, full_name="John", position="Dev")
    client.force_authenticate(user=user)

    restaurant = Restaurant.objects.create(name="KFC")
    menu = Menu.objects.create(
        restaurant=restaurant, date=timezone.now().date(), dishes={"a": 1}
    )

    resp = client.post("/api/votes/", {"menu": menu.id}, format="json")

    assert resp.status_code == 201
    assert Vote.objects.filter(employee=emp, menu=menu).exists()


@pytest.mark.django_db
def test_vote_twice_fails():
    client = APIClient()

    user = User.objects.create_user(username="u1", password="pass12345")
    emp = Employee.objects.create(user=user, full_name="John", position="Dev")
    client.force_authenticate(user=user)

    restaurant = Restaurant.objects.create(name="KFC")

    today = timezone.now().date()
    menu = Menu.objects.create(restaurant=restaurant, date=today, dishes={"x": 1})

    Vote.objects.create(employee=emp, menu=menu, date=today)

    resp = client.post("/api/votes/", {"menu": menu.id}, format="json")

    assert resp.status_code == 400
    assert "already voted" in resp.data["detail"].lower()


@pytest.mark.django_db
def test_vote_wrong_date_fails():
    client = APIClient()

    user = User.objects.create_user(username="u1", password="pass12345")
    Employee.objects.create(user=user, full_name="John", position="Dev")
    client.force_authenticate(user=user)

    restaurant = Restaurant.objects.create(name="KFC")

    yesterday = timezone.now().date() - timezone.timedelta(days=1)

    menu = Menu.objects.create(
        restaurant=restaurant,
        date=yesterday,
        dishes={"a": 1},
    )

    resp = client.post("/api/votes/", {"menu": menu.id}, format="json")

    assert resp.status_code == 400
    assert "only for today" in resp.data["detail"].lower()
