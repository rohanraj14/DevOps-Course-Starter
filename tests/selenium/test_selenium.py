import os
import pytest
import dotenv

from trello.trello_service import create_trello_board,delete_trello_board
from app import create_app
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread

@pytest.fixture(scope='module')
def test_app():
    # Use our .env config for selinium test instead of the test version
    file_path = dotenv.find_dotenv('.env')
    dotenv.load_dotenv(file_path, override=True)
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
    #Set Card name in input box
    card_name = driver.find_element_by_xpath("//*[@id='item']")
    card_name.send_keys('MyTask')
    #click button to create card
    driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

    #check queue header
    head1 = driver.find_elements_by_xpath("//h2[@class='mt-3']")
    assert head1[0].text == "Tasks in queue"
    
    #get title of task in To Do block and check the badge marked
    divs = driver.find_elements_by_xpath("//div[@class='container border boder-thik border-info']/div[@class='row row-cols-1 row-cols-sm-2 row-cols-md-4']/div[@class='col-md-4 pb-4']/div[@class='card border   border-info  ']/div[@class='card-header']/div[@class='row']/div[@class='col-md-9']/h5")
    for div in divs:
        task_title = div.text
    assert task_title == 'MyTask'
    
    #Badge on task marked as To Do
    sdivs = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class=' badge   badge-info ']")))
    status_label = sdivs[0].text
    assert status_label == 'To Do'

    #Send task to in progress
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Start"))).click()

    #get title of task in Doing list
    divs = driver.find_elements_by_xpath("//div[@class='container border boder-thik border-primary']/div[@class='row row-cols-1 row-cols-sm-2 row-cols-md-4']/div[@class='col-md-4 pb-4']/div[@class='card border  border-primary  ']/div[@class='card-header']/div[@class='row']/div[@class='col-md-9']/h5")
    for div in divs:
        task_title1 = div.text
    assert task_title1 == 'MyTask'

    sdivs = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class=' badge  badge-primary ']")))
    
    #Badge on task marked as To Do
    status_label = sdivs[0].text
    assert status_label == 'Doing'

    #Send task to Complete state
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Complete"))).click()

    #Restart the task - mark incomplete
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Start Again"))).click()




