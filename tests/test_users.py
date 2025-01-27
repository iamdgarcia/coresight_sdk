import pytest
from coresight_sdk.users import Users

@pytest.fixture
def mock_request_handler(mocker):
    return mocker.Mock()

@pytest.fixture
def users(mock_request_handler):
    return Users(mock_request_handler)

def test_create_anonymous_user(users, mock_request_handler):
    mock_response = {"user_id": "uuid-user", "session_id": "session-123"}
    mock_request_handler.post.return_value = mock_response

    response = users.create_anonymous(project_id="uuid-project", session_id="session-123")
    assert response == mock_response
    mock_request_handler.post.assert_called_once_with(
        "/projects/uuid-project/anonymous-users", {"session_id": "session-123"}
    )

def test_create_authenticated_user(users, mock_request_handler):
    mock_response = {"user_id": "uuid-user", "email": "user@example.com"}
    mock_request_handler.post.return_value = mock_response

    response = users.create_authenticated(
        project_id="uuid-project",
        email="user@example.com",
        name="John Doe",
        metadata={"role": "admin"}
    )
    assert response == mock_response
    mock_request_handler.post.assert_called_once_with(
        "/projects/uuid-project/authenticated-users",
        {"email": "user@example.com", "name": "John Doe", "metadata": {"role": "admin"}}
    )
