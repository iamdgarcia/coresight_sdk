import pytest
from coresight_sdk.messages import Messages

@pytest.fixture
def mock_request_handler(mocker):
    return mocker.Mock()

@pytest.fixture
def messages(mock_request_handler):
    return Messages(mock_request_handler)

def test_create_message(messages, mock_request_handler):
    mock_response = {"message_id": "uuid-message", "content": "Hello"}
    mock_request_handler.post.return_value = mock_response

    response = messages.create(
        project_id="uuid-project",
        thread_id="uuid-thread",
        sender_id="uuid-user",
        content="Hello"
    )
    assert response == mock_response
    mock_request_handler.post.assert_called_once_with(
        "/projects/uuid-project/threads/uuid-thread/messages",
        {"sender_id": "uuid-user", "content": "Hello"}
    )
