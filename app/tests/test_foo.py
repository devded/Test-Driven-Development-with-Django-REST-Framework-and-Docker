# app/tests/test_foo.py
import json
from django.urls import reverse


def test_hello_world():
    assert "foo" != "bar"


def test_ping(client):
    url = reverse("ping_name_for_reversing")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["ping"] == "pong"
