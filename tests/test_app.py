import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest, json
from app import create_app


@pytest.fixture
def client():
    c = create_app()
    yield c.test_client()


def test_difference_input(client):
    resp = client.get("/difference")
    assert resp.status_code == 400

    resp = client.get("/difference?number=-1")
    assert resp.status_code == 400

    resp = client.get("/difference?number=101")
    assert resp.status_code == 400

    resp = client.get("/difference?number=1")
    assert resp.status_code == 200


def test_difference(client):
    resp = client.get("/difference?number=10")
    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    payload = json.loads(resp.data)
    assert int(payload["value"]) == 2640
    assert int(payload["occurrences"] == 1)

    resp = client.get("/difference?number=10")
    resp = client.get("/difference?number=10")
    payload = json.loads(resp.data)
    assert int(payload["occurrences"] == 3)

    resp = client.get("/difference?number=1")
    payload = json.loads(resp.data)
    assert int(payload["occurrences"] == 1)
