# tests/unit/test_health.py
import pytest
from django.urls import reverse
 
@pytest.mark.django_db
def test_health_check_ok(client):
    response = client.get(reverse('health_check'))
    assert response.status_code == 200
    assert response.json()['checks']['database'] == 'ok'
 
@pytest.mark.django_db
def test_health_check_returns_json(client):
    response = client.get(reverse('health_check'))
    assert response['Content-Type'] == 'application/json'
