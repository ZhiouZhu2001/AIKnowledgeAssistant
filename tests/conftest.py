import pytest
from fastapi.testclient import TestClient

from ai_knowledge_assistant.main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client