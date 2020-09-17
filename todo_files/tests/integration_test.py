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
    # Replace call to requests.get(url) with our ownfunction
    mock_get_requests.side_effect = mock_get_cards
    response = client.get('/')


def mock_get_cards(url):
    sample_trello_lists_response = [{'id': '5f359ffd7ae1da360805ccad', 'checkItemStates': None, 'closed': False, 'dateLastActivity': '2020-08-13T20:18:05.529Z', 'desc': '', 'descData': None, 'dueReminder': None, 'idBoard': '5f3169dff2ad7b72d45fc4c3', 'idList': '5f3169df33611522761de7cc', 'idMembersVoted': [], 'idShort': 32, 'idAttachmentCover': None, 'idLabels': [], 'manualCoverAttachment': False, 'name': 'make a screen to edit the card details', 'pos': 81920, 'shortLink': 'dYitCLhv', 'isTemplate': False, 'badges': {'attachmentsByType': {'trello': {'board': 0, 'card': 0}}, 'location': False, 'votes': 0, 'viewingMemberVoted': False, 'subscribed': False, 'fogbugz': '', 'checkItems': 0, 'checkItemsChecked': 0, 'checkItemsEarliestDue': None, 'comments': 0, 'attachments': 0, 'description': False, 'due': None, 'dueComplete': False, 'start': None}, 'dueComplete': False, 'due': None, 'idChecklists': ['5f3be843afb729266e4a58c6'], 'idMembers': [], 'labels': [], 'shortUrl': 'https://trello.com/c/dYitCLhv', 'start': None, 'subscribed': False, 'url': 'https://trello.com/c/dYitCLhv/32-make-a-screen-to-edit-the-card-details', 'cover': {'idAttachment': None, 'color': None, 'idUploadedBackground': None, 'size': 'normal', 'brightness': 'light'}}, {'id': '5f3bde65142f2e7f87964ca5', 'checkItemStates': None, 'closed': False, 'dateLastActivity': '2020-08-18T13:57:57.970Z', 'desc': 'currently looks bad', 'descData': None, 'dueReminder': None, 'idBoard': '5f3169dff2ad7b72d45fc4c3', 'idList': '5f3169df33611522761de7cc', 'idMembersVoted': [], 'idShort': 47, 'idAttachmentCover': None, 'idLabels': [], 'manualCoverAttachment': False, 'name': 'use proper case when printing anything?', 'pos': 114688, 'shortLink': 'ClmV95mF', 'isTemplate': False, 'badges': {'attachmentsByType': {'trello': {'board': 0, 'card': 0}}, 'location': False, 'votes': 0, 'viewingMemberVoted': False, 'subscribed': False, 'fogbugz': '', 'checkItems': 0, 'checkItemsChecked': 0, 'checkItemsEarliestDue': None, 'comments': 0, 'attachments': 0, 'description': True, 'due': None, 'dueComplete': False, 'start': None}, 'dueComplete': False, 'due': None, 'idChecklists': [], 'idMembers': [], 'labels': [], 'shortUrl': 'https://trello.com/c/ClmV95mF', 'start': None, 'subscribed': False, 'url': 'https://trello.com/c/ClmV95mF/47-use-proper-case-when-printing-anything', 'cover': {'idAttachment': None, 'color': None, 'idUploadedBackground': None, 'size': 'normal', 'brightness': 'light'}}]
    
    if ('lists/5f3169e0916e3156fd3d1680/cards' in url
    or 'lists/5f3169df33611522761de7cc/cards' in url 
    or 'lists/5f3169dff5e94e5d22ec1d0f/cards' in url):
        response = Mock()
        response.json.return_value = sample_trello_lists_response
        return response
    return None 
