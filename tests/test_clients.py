import pytest
from coresight_sdk.client import CoresightClient
from coresight_sdk.utils import APIRequestHandler
from coresight_sdk.exceptions import ApiException

@pytest.fixture
def client():
    return CoresightClient(base_url="https://api.example.com", api_key="test-api-key")

def test_client_initialization(client):
    assert client.base_url == "https://api.example.com"
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
