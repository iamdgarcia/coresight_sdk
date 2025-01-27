import pytest
from coresight_sdk.client import ProjectClient
from coresight_sdk.utils import APIRequestHandler

@pytest.fixture
def client():
    return ProjectClient(api_key="test-api-key")

def test_client_initialization(client):
    assert client.api_key == "test-api-key"

def test_request_handler_headers(client):
    headers = client.request_handler._get_headers()
    assert headers["Content-Type"] == "application/json"
    assert headers["x-api-key"] == "test-api-key"

def test_health_check(mocker, client):
    mock_response = {"status": "healthy"}
    mocker.patch.object(APIRequestHandler, "get", return_value=mock_response)

    response = client.health_check()
    assert response == mock_response
