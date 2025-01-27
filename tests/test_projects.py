import pytest
from coresight_sdk.projects import Projects

@pytest.fixture
def mock_request_handler(mocker):
    return mocker.Mock()

@pytest.fixture
def projects(mock_request_handler):
    return Projects(mock_request_handler)

def test_create_project(projects, mock_request_handler):
    mock_response = {"project_id": "uuid-project", "name": "Test Project"}
    mock_request_handler.post.return_value = mock_response

    response = projects.create(name="Test Project", llm_config={"model": "gpt-4"})
    assert response == mock_response
    mock_request_handler.post.assert_called_once_with(
        "/projects", {"name": "Test Project", "llm_config": {"model": "gpt-4"}}
    )

def test_get_project(projects, mock_request_handler):
    mock_response = {"project_id": "uuid-project", "name": "Test Project"}
    mock_request_handler.get.return_value = mock_response

    response = projects.get(project_id="uuid-project")
    assert response == mock_response
    mock_request_handler.get.assert_called_once_with("/projects/uuid-project")
