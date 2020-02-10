import django
import pytest

from django.test import RequestFactory

from rest_framework.test import APIClient


def pytest_configure():
    django.setup()


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def api_client():
    return APIClient()
