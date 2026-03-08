import pytest
from fastapi.testclient import TestClient
from app.main import app
import redis

# Create test client
client = TestClient(app)

# Connect to Redis (make sure docker-compose has redis running)
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@pytest.fixture(autouse=True)
def clear_redis():
    """Clear Redis counter before each test"""
    r.flushdb()
    yield
    r.flushdb()


def test_read_root():
    """Test GET /"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DevOps Demo"}


def test_get_counter_initial():
    """Counter should start at 0"""
    response = client.get("/counter")
    assert response.status_code == 200
    assert response.json()["counter"] == 0


def test_increment_counter():
    """Test POST /counter increments the counter"""
    # First increment
    response = client.post("/counter")
    assert response.status_code == 200
    assert response.json()["counter"] == 1

    # Second increment
    response = client.post("/counter")
    assert response.json()["counter"] == 2

    # Check GET /counter
    response = client.get("/counter")
    assert response.json()["counter"] == 2