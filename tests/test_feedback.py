import pytest
from coresight_sdk.feedback import Feedback

@pytest.fixture
def mock_request_handler(mocker):
    return mocker.Mock()

@pytest.fixture
def feedback(mock_request_handler):
    return Feedback(mock_request_handler)

def test_add_feedback(feedback, mock_request_handler):
    mock_response = {"feedback_id": "uuid-feedback"}
    mock_request_handler.post.return_value = mock_response

    response = feedback.add(
        project_id="uuid-project",
        message_id="uuid-message",
        user_id="uuid-user",
        rating=5,
        comment="Great message!"
    )
    assert response == mock_response
    mock_request_handler.post.assert_called_once_with(
        "/projects/uuid-project/messages/uuid-message/feedback",
        {"user_id": "uuid-user", "rating": 5, "comment": "Great message!"}
    )

def test_list_feedback(feedback, mock_request_handler):
    mock_response = [{"feedback_id": "uuid-feedback", "rating": 5}]
    mock_request_handler.get.return_value = mock_response

    response = feedback.list(project_id="uuid-project", message_id="uuid-message")
    assert response == mock_response
    mock_request_handler.get.assert_called_once_with(
        "/projects/uuid-project/messages/uuid-message/feedback"
    )
