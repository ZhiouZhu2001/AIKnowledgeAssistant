from fastapi.testclient import TestClient

def test_health_check(client: TestClient):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_none_exists_endoint(client: TestClient):
    response = client.get("/nonexistent")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_reject_post_request_to_health_endpoint(client: TestClient):
    response = client.post("/health")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_health_return_json(client: TestClient):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"