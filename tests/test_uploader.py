from django.test import Client
from django.urls import reverse


def test_gallery_non_authenticated(client: Client) -> None:
    """Make sure users API not available for non-authenticated requests."""
    response = client.get(reverse('gallery'))
    assert response.status_code == 403


def test_gallery(admin_client: Client) -> None:
    """Gallery GET test."""
    response = admin_client.get(reverse('gallery'))
    assert response.status_code == 200
