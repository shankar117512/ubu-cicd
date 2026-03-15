from django.urls import reverse

def test_root_url(client):
    response = client.get("/")
    assert response.status_code in [200, 301, 302]
