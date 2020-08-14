from flask import session
import os
import requests

# debug = True
debug = False
todoList = "5f3169df33611522761de7cc"
doingList = "5f3169e0916e3156fd3d1680"
doneList = "5f3169dff5e94e5d22ec1d0f"
trelloBoard = "5f3169dff2ad7b72d45fc4c3"


def get_cards():
    todo = get_trello("https://api.trello.com/1/lists/" + todoList + "/cards?")
    doing = get_trello("https://api.trello.com/1/lists/" + doingList + "/cards?")
    done = get_trello("https://api.trello.com/1/lists/" + doneList + "/cards?")

    if debug:
        print("cards - ")
        print(todo)
        print(doing)
        print(done)
        print("boards - ")
        print(get_trello("https://api.trello.com/1/members/me/boards?"))
        print("lists - ")
        print(get_trello("https://api.trello.com/1/boards/" + trelloBoard + "/lists?"))

    return todo, doing, done


def get_card(id):
    items, doing, done = get_cards()
    items = items + doing + done
    return next((item for item in items if item['id'] == id), None)


def add_card(title, desc, dueDate):
    post_trello(
        "https://api.trello.com/1/cards?idList=" + todoList + "&name=" + title + "&desc=" + desc + "&due=" + dueDate)


def add_checklist_item(id, title):
    checklists = get_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
    print(checklists[0]["id"])
    post_trello("https://api.trello.com/1/checklists/" + checklists[0]["id"] + "/checkItems/?name=" + title)


def set_card_to_complete(id):
    put_trello("https://api.trello.com/1/cards/" + id + "/?idList=" + doneList)


def complete_checklist_item(id, checklist_id):
    put_trello("https://api.trello.com/1/cards/" + id + "/checkItem/" + checklist_id + "/?state=complete")


def delete_card(id):
    delete_trello("https://api.trello.com/1/cards/" + id + "?")


def delete_checklist_item(id, checklist_id):
    delete_trello("https://api.trello.com/1/cards/" + id + "/checkItem/" + checklist_id + "/?")


def set_card_in_progress(id):
    put_trello("https://api.trello.com/1/cards/" + id + "/?idList=" + doingList)


def get_card_checklist(id):
    todo = get_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
    if todo:
        return todo[0]["checkItems"]
    else:
        post_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
        todo = get_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
        return todo[0]["checkItems"]


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
