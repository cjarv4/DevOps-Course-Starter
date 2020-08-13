from flask import session
import os
import requests

# debug = True
debug = False


def get_items():
    cards, doing, done = get_cards()

    if debug:
        print("cards - ")
        print(cards)
        print(doing)
        print(done)
        print("boards - ")
        get_boards()
        print("lists - ")
        get_lists()
    return cards, doing, done


def get_item(id):
    items, doing, done = get_items()
    items = items + doing + done
    return next((item for item in items if item['id'] == id), None)


def add_item(title):
    post_trello("https://api.trello.com/1/cards?idList=5f3169df33611522761de7cc&name=" + title)


def complete_item(id):
    put_trello("https://api.trello.com/1/cards/" + id + "/?idList=5f3169dff5e94e5d22ec1d0f")


def complete_checklist_item(id, checklist_id):
    put_trello("https://api.trello.com/1/cards/" + id + "/checkItem/" + checklist_id + "/?state=complete")


def delete_item(id):
    delete_trello("https://api.trello.com/1/cards/" + id + "?")


def delete_checklist_item(id, checklist_id):
    delete_trello("https://api.trello.com/1/cards/" + id + "/checkItem/" + checklist_id + "/?")


def get_boards():
    response = get_trello("https://api.trello.com/1/members/me/boards?")
    print(response)


def get_lists():
    response = get_trello("https://api.trello.com/1/boards/5f3169dff2ad7b72d45fc4c3/lists?")
    print(response)


def get_cards():
    todo = get_trello("https://api.trello.com/1/lists/5f3169df33611522761de7cc/cards?")
    doing = get_trello("https://api.trello.com/1/lists/5f3169e0916e3156fd3d1680/cards?fields=id,closed,name")
    done = get_trello("https://api.trello.com/1/lists/5f3169dff5e94e5d22ec1d0f/cards?fields=id,closed,name")

    return todo, doing, done


def get_card_checklist(id):
    todo = get_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
    if todo:
        return todo[0]["checkItems"]
    else:
        return [{"name": "Empty checklist - add a checklist item", 'state': 'Incomplete'}]


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
