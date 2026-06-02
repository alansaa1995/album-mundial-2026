import pytest


class TestInventory:
    def test_add_sticker_obtained(self, client, seed_stickers, registered_user):
        user_id = registered_user["id"]
        response = client.post(f"/api/v1/inventory/{user_id}/sticker", json={
            "sticker_code": "ARG1",
            "action": "obtained",
        })
        assert response.status_code == 200
        data = response.json()
        assert data["is_pasted"] is True
        assert data["quantity"] == 1
        assert data["sticker"]["code"] == "ARG1"

    def test_add_sticker_repeated(self, client, seed_stickers, registered_user):
        user_id = registered_user["id"]
        response = client.post(f"/api/v1/inventory/{user_id}/sticker", json={
            "sticker_code": "BRA1",
            "action": "repeated",
        })
        assert response.status_code == 200
        data = response.json()
        assert data["is_pasted"] is False
        assert data["quantity"] == 1

    def test_duplicate_increments_quantity(self, client, seed_stickers, registered_user):
        user_id = registered_user["id"]
        payload = {"sticker_code": "ARG2", "action": "repeated"}
        client.post(f"/api/v1/inventory/{user_id}/sticker", json=payload)
        response = client.post(f"/api/v1/inventory/{user_id}/sticker", json=payload)
        assert response.status_code == 200
        assert response.json()["quantity"] == 2

    def test_add_sticker_unknown_code(self, client, seed_stickers, registered_user):
        user_id = registered_user["id"]
        response = client.post(f"/api/v1/inventory/{user_id}/sticker", json={
            "sticker_code": "NOEXISTE",
            "action": "obtained",
        })
        assert response.status_code == 404

    def test_add_sticker_invalid_action(self, client, seed_stickers, registered_user):
        user_id = registered_user["id"]
        response = client.post(f"/api/v1/inventory/{user_id}/sticker", json={
            "sticker_code": "ARG1",
            "action": "invalid_action",
        })
        assert response.status_code == 422

    def test_get_album_progress_empty(self, client, seed_stickers, registered_user):
        user_id = registered_user["id"]
        response = client.get(f"/api/v1/inventory/{user_id}/progress")
        assert response.status_code == 200
        data = response.json()
        assert data["pasted_stickers"] == 0
        assert data["completion_percentage"] == 0.0
        assert data["total_stickers"] == len(seed_stickers)

    def test_get_album_progress_with_stickers(self, client, seed_stickers, registered_user):
        user_id = registered_user["id"]
        # Pegar 2 figuritas
        for code in ["ARG1", "BRA1"]:
            client.post(f"/api/v1/inventory/{user_id}/sticker", json={
                "sticker_code": code,
                "action": "obtained",
            })
        # Agregar 1 repetida
        client.post(f"/api/v1/inventory/{user_id}/sticker", json={
            "sticker_code": "ARG2",
            "action": "repeated",
        })

        response = client.get(f"/api/v1/inventory/{user_id}/progress")
        assert response.status_code == 200
        data = response.json()
        assert data["pasted_stickers"] == 2
        assert data["completion_percentage"] == 50.0  # 2/4 stickers de seed
        assert len(data["duplicates"]) == 1
        assert data["duplicates"][0]["sticker"]["code"] == "ARG2"

    def test_progress_user_not_found(self, client):
        response = client.get("/api/v1/inventory/99999/progress")
        assert response.status_code == 404

    def test_health_endpoint(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
