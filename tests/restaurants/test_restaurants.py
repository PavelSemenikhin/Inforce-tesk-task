import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from restaurants.models import Restaurant

User = get_user_model()


@pytest.mark.django_db
def test_restaurant_list_requires_auth():
    client = APIClient()

    response = client.get("/api/restaurants/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_restaurant_list_success():
    Restaurant.objects.create(name="KFC")
    Restaurant.objects.create(name="McDonalds")

    user = User.objects.create_user(username="u1", password="pass12345")

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/restaurants/")
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_create_restaurant_admin_only():
    user = User.objects.create_user(username="u1", password="pass12345")

    client = APIClient()
    client.force_authenticate(user=user)

    payload = {"name": "KFC"}
    response = client.post("/api/restaurants/", payload)

    assert response.status_code == 403


@pytest.mark.django_db
def test_create_restaurant_success():
    admin = User.objects.create_superuser(username="admin", password="pass12345")

    client = APIClient()
    client.force_authenticate(user=admin)

    payload = {"name": "KFC"}
    response = client.post("/api/restaurants/", payload)

    assert response.status_code == 201
    assert Restaurant.objects.filter(name="KFC").exists()


@pytest.mark.django_db
def test_create_restaurant_invalid_data():
    admin = User.objects.create_superuser(username="admin", password="pass12345")

    client = APIClient()
    client.force_authenticate(user=admin)

    payload = {"name": ""}
    response = client.post("/api/restaurants/", payload)

    assert response.status_code == 400
