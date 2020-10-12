from trello.trello_cards import Item
import os
import json
import requests 

TRELLO_SERVICE_ENDPOINT=os.environ.get('TRELLO_URL')
def get_auth_params():
    return {    
                'key': os.environ.get('TRELLO_KEY'), 
                'token': os.environ.get('TRELLO_TOKEN') 
            }

def get_boards_url():
    return TRELLO_SERVICE_ENDPOINT+'/members/me/boards'

def get_list_from_board_url(boardID):
    return TRELLO_SERVICE_ENDPOINT+'/boards/'+boardID+'/lists'

def create_card_url():
     return TRELLO_SERVICE_ENDPOINT+'/cards'

def get_cards_of_list_url(listId):
     return TRELLO_SERVICE_ENDPOINT+'/lists/'+listId+'/cards'

def move_card_url(cardId):
     return (TRELLO_SERVICE_ENDPOINT+'/cards/%s' % cardId)


def get_all_boards():
    response = requests.request("GET", get_boards_url(), params=get_auth_params())
    boards = response.json()
    return boards

def get_board_by_name(name):
    boards = get_all_boards()
    return next((board for board in boards if board['name'] == name), None)

def get_all_lists():
    url = get_list_from_board_url(os.environ.get('TRELLO_BOARD_ID'))
    
    response = requests.get(url, params = get_auth_params())
    lists = response.json()
    return lists

def get_list_by_name(name):
    lists = get_all_lists()
    return next((lister for lister in lists if lister['name'] == name), None)

def add_card_by_name(name):
    todo_list = get_list_by_name('To Do')
    extra_params = { 'name': name, 'idList': todo_list['id'] }
    params = get_auth_params()
    params.update(extra_params)
    url = create_card_url()
    print(params)
    response = requests.post(url, params = params)
    card = response.json()
    return Item.trelloCard(card, todo_list)

def get_cards_by_list_name(name):
    todo_list = get_list_by_name(name)
    params = get_auth_params()
    url = get_cards_of_list_url(todo_list['id'])

    response = requests.get(url, params = params)
    cards = response.json()
    return cards


def get_all_cards():
    lists = get_all_lists()
    cards = []

    for card_list in lists:
        list_cards = get_cards_by_list_name(card_list['name'])
        for card in list_cards:
            cards.append(Item.trelloCard(card, card_list))
    return cards


def get_card_by_id(id):
    cards = get_all_cards()
    return next((card for card in cards if card['id'] == id), None)


def move_card_to_new_list(card_id, to_list_name):
    to_list=get_list_by_name(to_list_name)
    extra_params = { 'idList': to_list['id'] }
    params = get_auth_params()
    params.update(extra_params)
    url = move_card_url(card_id)

    response = requests.put(url, params = params)
    card = response.json()

    return card