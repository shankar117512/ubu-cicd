import pytest
from django.test import Client
from django.contrib.auth import get_user_model
 
User = get_user_model()
 
@pytest.fixture
def api_client():
    return Client()
 
@pytest.fixture
def test_user(db):
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
 
@pytest.fixture
def auth_client(api_client, test_user):
    api_client.force_login(test_user)
    return api_client
