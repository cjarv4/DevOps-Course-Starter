import os
import requests

todoList = "5f3169df33611522761de7cc"
doingList = "5f3169e0916e3156fd3d1680"
doneList = "5f3169dff5e94e5d22ec1d0f"
trelloBoard = "5f3169dff2ad7b72d45fc4c3"


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
