import pytest
from coresight_sdk.subscriptions import Subscriptions

@pytest.fixture
def mock_request_handler(mocker):
    return mocker.Mock()

@pytest.fixture
def subscriptions(mock_request_handler):
    return Subscriptions(mock_request_handler)

def test_create_subscription(subscriptions, mock_request_handler):
    mock_response = {"subscription_id": "uuid-subscription"}
    mock_request_handler.post.return_value = mock_response

    response = subscriptions.create(client_id="uuid-client", price_id="price-123", plan="Premium")
    assert response == mock_response
    mock_request_handler.post.assert_called_once_with(
        "/clients/uuid-client/subscriptions",
        {"price_id": "price-123", "plan": "Premium"}
    )

def test_cancel_subscription(subscriptions, mock_request_handler):
    mock_response = {"message": "Subscription canceled successfully"}
    mock_request_handler.delete.return_value = mock_response

    response = subscriptions.cancel(subscription_id="uuid-subscription")
    assert response == mock_response
    mock_request_handler.delete.assert_called_once_with("/subscriptions/uuid-subscription")
