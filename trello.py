import os
import requests

host = "https://api.trello.com/1/"


def get_trello_board_id():
    board = get_trello("members/me/boards?")
    return board[0]["id"]


def get_trello(url):
    url = add_trello_host_token_and_key(url)
    response = requests.get(url=url).json()
    return response


def add_trello_host_token_and_key(url):
    return host + url + "&token=" + os.getenv(
        'TRELLO_TOKEN') + "&key=" + os.getenv('TRELLO_KEY')


boardId = get_trello_board_id()


def post_trello(url):
    url = add_trello_host_token_and_key(url)
    response = requests.post(url=url)
    return response


def put_trello(url):
    url = add_trello_host_token_and_key(url)
    response = requests.put(url=url)
    return response


def delete_trello(url):
    url = add_trello_host_token_and_key(url)
    response = requests.delete(url=url)
    return response


def get_trello_list_id(name):
    lists = get_trello("boards/" + boardId + "/lists?")
    list = next((list for list in lists if list["name"] == name), None)
    return list["id"]
