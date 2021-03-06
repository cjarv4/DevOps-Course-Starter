import pytest
import trello
import app
import card
import view_model
import board

from datetime import datetime

# Get a stub card

def create_test_card(title):
    card.add_card(title=title, desc="made for testing", dueDate="")

def cleanup_test_card(title):
    test_card = card.get_card_by_name(title)
    card.delete_card(test_card.id)

def cleanup_test_board(name):
    test_board = board.get_board_by_name(name)
    board.delete_board(test_board.id)

def test_trello_connection():
    response = trello.get_trello_board_id()
    assert response=='5f3169dff2ad7b72d45fc4c3'

def test_get_individual_lists_and_convert_to_objects():
    todo, doing, done = card.get_cards()
    assert isinstance(todo, list)
    assert isinstance(doing, list)
    assert isinstance(done, list)

def test_create_and_clear_down_card():
    test_card_name = "test_create_then_clear_down"
    try:
        create_test_card(test_card_name)
        test_card = card.get_card_by_name(test_card_name)
        assert test_card.name==test_card_name
    finally:
        cleanup_test_card(test_card_name)
        test_card = card.get_card_by_name(test_card_name)
        assert test_card == None

def test_get_card_last_modified_date():
    test_card_name = "test_get_card_last_modified_date"
    try:
        create_test_card(test_card_name)
        test_card = card.get_card_by_name(test_card_name)
        assert test_card.last_activity
    finally:
        cleanup_test_card(test_card_name)

def test_return_all_done():
    todo, doing, done = card.get_cards()

    item_view_model = view_model.ViewModel(todo, doing, done, True)
    assert len(done)==len(item_view_model.done)

def test_return_todays_done():
    test_card_name="test_done_returns_today_only"
    try:
        create_test_card(test_card_name)
        test_card = card.get_card_by_name(test_card_name)
        card.set_card_to_complete(test_card.id)

        todo, doing, done = card.get_cards()
        item_view_model = view_model.ViewModel(todo, doing, done, False)
        assert len(item_view_model.done)>=1 and len(item_view_model.done)<=len(done)
    finally:
        cleanup_test_card(test_card_name)

def test_create_and_clear_down_board():
    test_board_name = "test_create_then_clear_down"
    try:
        board.add_board(test_board_name)
        test_board = board.get_board_by_name(test_board_name)
        assert test_board.name==test_board_name
    finally:
        cleanup_test_board(test_board_name)
        test_board = board.get_board_by_name(test_board_name)
        assert test_board == None