import os
from threading import Thread
import pytest
import Board as board
import app
from selenium import webdriver

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    new_board = board.add_board("selenium_test_board")
    os.environ['TRELLO_BOARD_ID'] = new_board.id

    # construct the new application
    application = app.create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app

    # Tear Down
    thread.join(1)
    board.delete_board(new_board.id)

@pytest.fixture(scope="module")
def driver():
    # browser = webdriver.Firefox(executable_path=r'geckodriver')
    with webdriver.Firefox(executable_path=r'/Users/cjarv4/Downloads/geckodriver') as driver:
        yield driver

def test_task_journey(driver, test_app): 
    # os.environ["PATH"] += os.pathsep + '/Users/cjarv4/Downloads/'
    
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'