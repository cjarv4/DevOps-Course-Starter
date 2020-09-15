import os
import requests
from dotenv import load_dotenv


def get_trello_board_id():
    board = get_trello("members/me/boards?")
    return board[0]["id"]


def get_trello(url):
    url = add_trello_host_token_and_key(url)
    response = requests.get(url)
    response_json = response.json()
    return response_json


def add_trello_host_token_and_key(url):
    host = "https://api.trello.com/1/"
    load_dotenv()
    return str(host) + str(url) + "&token=" + os.getenv('TRELLO_TOKEN') + "&key=" + os.getenv('TRELLO_KEY')


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
    boardId = get_trello_board_id()
    lists = get_trello("boards/" + boardId + "/lists?")
    list = next((list for list in lists if list["name"] == name), None)
    return list["id"]
