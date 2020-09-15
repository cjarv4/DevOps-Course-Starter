import pytest
import trello as trello
import Card as card

def test_first():
    print("testing")
    assert 1==1

def test_trello_connection():
    response = trello.get_trello_board_id()
    assert response=='5f3169dff2ad7b72d45fc4c3'

def test_get_individual_lists():
    todo, doing, done = card.get_cards()
    assert isinstance(todo, list)
    assert isinstance(doing, list)
    assert isinstance(done, list)