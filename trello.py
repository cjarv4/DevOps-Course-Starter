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
