import os
import pytest
from trello.trello_service import create_trello_board,delete_trello_board
from app import create_app
from selenium import webdriver
from threading import Thread

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id
    # construct the new application
    application = create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application
    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)



@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')

    assert driver.title == 'Trello Board'
    #Get board name created
    board_name = driver.find_element_by_xpath("//h1[@class='display-4']").text
    assert board_name == 'To-Do App'