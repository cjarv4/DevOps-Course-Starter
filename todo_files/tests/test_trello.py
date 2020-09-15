import pytest
import trello as trello
import Card as card

# Get a stub card

def create_test_card(title):
    card.add_card(title=title, desc="made for testing", dueDate="")

def cleanup_test_card(title):
    test_card = card.get_card_by_name(title)
    card.delete_card(test_card.id)

def test_trello_connection():
    response = trello.get_trello_board_id()
    assert response=='5f3169dff2ad7b72d45fc4c3'

def test_get_individual_lists():
    todo, doing, done = card.get_cards()
    assert isinstance(todo, list)
    assert isinstance(doing, list)
    assert isinstance(done, list)

def test_get_card_last_modified_date():
    test_card_name = "test_get_card_last_modified_date"
    try:
        create_test_card(test_card_name)
        test_card = card.get_card_by_name(test_card_name)
        assert test_card.last_activity
    finally:
        cleanup_test_card(test_card_name)
