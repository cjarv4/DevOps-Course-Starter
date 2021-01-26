import pytest
from dotenv import load_dotenv, find_dotenv
import app
from unittest.mock import patch, Mock


@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version 
    file_path = find_dotenv('/.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


@patch('requests.get')
def test_index_page(mock_get_requests, client):
    # Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_cards
    response = client.get('/')
    assert response.status_code == 200
    assert mock_get_requests.call_count == 3


def mock_get_cards(url):
    sample_trello_lists_response = [{'id': '5f359ffd7ae1da360805ccad', 'checkItemStates': None, 'closed': False,
                                     'dateLastActivity': '2020-08-13T20:18:05.529Z', 'desc': 'test', 'descData': None,
                                     'dueReminder': None, 'idBoard': '5f3169dff2ad7b72d45fc4c3',
                                     'idList': '5f3169df33611522761de7cc', 'idMembersVoted': [], 'idShort': 32,
                                     'idAttachmentCover': None, 'idLabels': [], 'manualCoverAttachment': False,
                                     'name': 'test', 'pos': 81920,
                                     'shortLink': 'dYitCLhv', 'isTemplate': False, 'dueComplete': False, 'due': None,
                                     'idChecklists': ['5f3be843afb729266e4a58c6']}]

    if ('lists/5f3169e0916e3156fd3d1680/cards' in url
            or 'lists/5f3169df33611522761de7cc/cards' in url
            or 'lists/5f3169dff5e94e5d22ec1d0f/cards' in url):
        response = Mock()
        response.json.return_value = sample_trello_lists_response
        return response
    return None


def test_flip_global_show_all_done(client):
    old_show_all = app.show_all_done
    # response = client.get('/showAll')
    assert old_show_all!=app.show_all_done