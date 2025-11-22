import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


User = get_user_model()


@pytest.mark.django_db
def test_employee_create_requires_auth():
    client = APIClient()

    payload = {"full_name": "John Doe", "position": "Dev"}
    response = client.post("/api/accounts/employees/", payload)

    assert response.status_code == 401
