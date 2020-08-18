import os
import requests


def get_trello(url):
    url = add_trello_token_and_key(url)
    response = requests.get(url=url).json()
    return response


def post_trello(url):
    url = add_trello_token_and_key(url)
    response = requests.post(url=url)
    return response


def put_trello(url):
    url = add_trello_token_and_key(url)
    response = requests.put(url=url)
    return response


def delete_trello(url):
    url = add_trello_token_and_key(url)
    response = requests.delete(url=url)
    return response


def add_trello_token_and_key(url):
    return url + "&token=" + os.getenv(
        'TRELLO_TOKEN') + "&key=" + os.getenv('TRELLO_KEY')


def get_trello_board_id():
    board = get_trello("https://api.trello.com/1/members/me/boards?")
    print("Got ID for Board")
    return board[0]["id"]

boardId = get_trello_board_id()

def get_trello_list_id(name):
    lists = get_trello("https://api.trello.com/1/boards/" + boardId + "/lists?")
    list = next((list for list in lists if list["name"] == name), None)
    print("Got ID for " + name)
    return list["id"]


