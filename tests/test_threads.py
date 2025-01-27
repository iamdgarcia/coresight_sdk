import pytest
from coresight_sdk.threads import Threads

@pytest.fixture
def mock_request_handler(mocker):
    return mocker.Mock()

@pytest.fixture
def threads(mock_request_handler):
    return Threads(mock_request_handler)

def test_create_thread(threads, mock_request_handler):
    mock_response = {"thread_id": "uuid-thread", "user_id": "uuid-user"}
    mock_request_handler.post.return_value = mock_response

    response = threads.create(user_id="uuid-user")
    assert response == mock_response
    mock_request_handler.post.assert_called_once_with("/threads", {"user_id": "uuid-user"})

def test_get_thread(threads, mock_request_handler):
    mock_response = {"thread_id": "uuid-thread", "user_id": "uuid-user"}
    mock_request_handler.get.return_value = mock_response

    response = threads.get(thread_id="uuid-thread")
    assert response == mock_response
    mock_request_handler.get.assert_called_once_with("/threads/uuid-thread")

def test_list_threads(threads, mock_request_handler):
    mock_response = [{"thread_id": "uuid-thread", "user_id": "uuid-user"}]
    mock_request_handler.get.return_value = mock_response

    response = threads.list()
    assert response == mock_response
    mock_request_handler.get.assert_called_once_with("/threads")
