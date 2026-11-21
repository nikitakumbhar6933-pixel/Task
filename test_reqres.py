import os
import requests
import pytest

pytestmark = pytest.mark.api
BASE = "https://reqres.in/api"
HEADERS = {}
if os.getenv("REQRES_API_KEY"):
    HEADERS["x-api-key"] = os.environ["REQRES_API_KEY"]

def get(path, **kwargs):
    return requests.get(f"{BASE}{path}", headers=HEADERS, timeout=20, **kwargs)

def post(path, **kwargs):
    return requests.post(f"{BASE}{path}", headers=HEADERS, timeout=20, **kwargs)

def test_get_users_success_and_schema():
    response = get("/users?page=2")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, dict)
    assert {"page", "per_page", "total", "total_pages", "data"}.issubset(body)
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0
    assert {"id", "email", "first_name", "last_name", "avatar"}.issubset(body["data"][0])

def test_get_single_user_success():
    response = get("/users/2")
    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert {"id", "email", "first_name", "last_name", "avatar"}.issubset(body["data"])

def test_post_create_user_success():
    payload = {"name": "qa automation", "job": "tester"}
    response = post("/users", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body.get("name") == payload["name"]
    assert body.get("job") == payload["job"]
    assert "id" in body and "createdAt" in body

def test_post_missing_data_validation():
    response = post("/register", json={"email": "sydney@fife"})
    assert response.status_code == 400
    body = response.json()
    assert isinstance(body, dict)
    assert "error" in body

def test_get_unknown_user_returns_404():
    response = get("/users/9999")
    assert response.status_code == 404
    assert response.text.strip() in ("", "{}") or isinstance(response.json(), dict)
