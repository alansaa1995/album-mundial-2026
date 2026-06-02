import pytest


class TestStickers:
    def test_list_stickers_empty(self, client):
        response = client.get("/api/v1/stickers/")
        assert response.status_code == 200
        assert response.json() == []

    def test_list_stickers_with_data(self, client, seed_stickers):
        response = client.get("/api/v1/stickers/")
        assert response.status_code == 200
        assert len(response.json()) == len(seed_stickers)

    def test_get_sticker_by_code(self, client, seed_stickers):
        response = client.get("/api/v1/stickers/ARG1")
        assert response.status_code == 200
        data = response.json()
        assert data["code"] == "ARG1"
        assert data["player_name"] == "Lionel Messi"

    def test_get_sticker_case_insensitive(self, client, seed_stickers):
        response = client.get("/api/v1/stickers/arg1")
        assert response.status_code == 200
        assert response.json()["code"] == "ARG1"

    def test_get_sticker_not_found(self, client):
        response = client.get("/api/v1/stickers/NOEXISTE")
        assert response.status_code == 404

    def test_special_sticker_flag(self, client, seed_stickers):
        response = client.get("/api/v1/stickers/EST1")
        assert response.status_code == 200
        assert response.json()["is_special"] is True
