import pytest
import dotenv
import app
import json
from trello import trello_service
from unittest.mock import Mock, patch
from patch_requests import patch_requests

with open('tests/response_mock.json') as mocklists:
  data = json.load(mocklists)
sample_response = json.dumps(data)

with open('tests/todo_response_mock.json') as mocktodo:
  data_todo = json.load(mocktodo)
sample_response_todo = json.dumps(data_todo)

with open('tests/doing_response_mock.json') as mockdoing:
  data_doing = json.load(mockdoing)
sample_response_doing = json.dumps(data_doing)

with open('tests/done_response_mock.json') as mockdone:
  data_done = json.load(mockdone)
sample_response_done = json.dumps(data_done)

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = dotenv.find_dotenv('.env.test')
    dotenv.load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client
        

def mock_get_lists(url, param):
    if url == 'http://api.trello.com/1/boards/5f5a958fa07c17615cc9e37f/lists' :
        mockresponse = Mock()
        mockresponse.json.return_value = sample_response
        return mockresponse
    elif url == 'http://api.trello.com/1/lists/5f5a958fa07c17615cc9e380/cards':
        mockresponse_todo = Mock()
        mockresponse_todo.json.return_value = sample_response_todo
        return mockresponse_todo
    elif url == 'http://api.trello.com/1/lists/5f5a958fa07c17615cc9e381/cards':
        mockresponse_doing = Mock()
        mockresponse_doing.json.return_value = sample_response_doing
        return mockresponse_doing
    elif url == 'http://api.trello.com/1/lists/5f5a958fa07c17615cc9e382/cards':
        mockresponse_done = Mock()
        mockresponse_done.json.return_value = sample_response_done
        return mockresponse_done
    return None

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    mock_get_requests.side_effect = mock_get_lists
    response = client.get('/')

    assert response.status_code == 200


