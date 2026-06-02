import pytest


class TestUserRegistration:
    def test_register_user_success(self, client):
        response = client.post("/api/v1/users/", json={
            "username": "messi10",
            "email": "messi@argentina.com",
            "password": "goat4ever",
        })
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == "messi10"
        assert data["email"] == "messi@argentina.com"
        assert "id" in data
        assert "hashed_password" not in data

    def test_register_duplicate_username(self, client):
        payload = {"username": "duplicado", "email": "a@test.com", "password": "pass"}
        client.post("/api/v1/users/", json=payload)
        response = client.post("/api/v1/users/", json={**payload, "email": "b@test.com"})
        assert response.status_code == 409
        assert "duplicado" in response.json()["detail"]

    def test_register_duplicate_email(self, client):
        payload = {"username": "user1", "email": "shared@test.com", "password": "pass"}
        client.post("/api/v1/users/", json=payload)
        response = client.post("/api/v1/users/", json={**payload, "username": "user2"})
        assert response.status_code == 409

    def test_register_short_username(self, client):
        response = client.post("/api/v1/users/", json={
            "username": "ab",
            "email": "short@test.com",
            "password": "pass",
        })
        assert response.status_code == 422

    def test_register_invalid_email(self, client):
        response = client.post("/api/v1/users/", json={
            "username": "validuser",
            "email": "not-an-email",
            "password": "pass",
        })
        assert response.status_code == 422

    def test_get_user_by_id(self, client, registered_user):
        user_id = registered_user["id"]
        response = client.get(f"/api/v1/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["id"] == user_id

    def test_get_user_not_found(self, client):
        response = client.get("/api/v1/users/99999")
        assert response.status_code == 404
