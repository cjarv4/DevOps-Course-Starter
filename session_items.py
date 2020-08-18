from flask import session
import os
import requests
import trello as trello

# debug = True
debug = False
todoList = "5f3169df33611522761de7cc"
doingList = "5f3169e0916e3156fd3d1680"
doneList = "5f3169dff5e94e5d22ec1d0f"
trelloBoard = "5f3169dff2ad7b72d45fc4c3"


def get_cards():
    todo = trello.get_trello("https://api.trello.com/1/lists/" + todoList + "/cards?")
    doing = trello.get_trello("https://api.trello.com/1/lists/" + doingList + "/cards?")
    done = trello.get_trello("https://api.trello.com/1/lists/" + doneList + "/cards?")

    if debug:
        print("cards - ")
        print(todo)
        print(doing)
        print(done)
        print("boards - ")
        print(trello.get_trello("https://api.trello.com/1/members/me/boards?"))
        print("lists - ")
        print(trello.get_trello("https://api.trello.com/1/boards/" + trelloBoard + "/lists?"))

    return todo, doing, done


def get_card(id):
    todo, doing, done = get_cards()
    cards = todo + doing + done
    card = next((card for card in cards if card['id'] == id), None)
    if card["due"]:
        card["due"] = card["due"][0:10] #ignore timestamp
    return card


def add_card(title, desc, dueDate):
    trello.post_trello(
        "https://api.trello.com/1/cards?idList=" + todoList + "&name=" + title + "&desc=" + desc + "&due=" + dueDate)


def add_checklist_item(id, title):
    checklists = trello.get_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
    print(checklists[0]["id"])
    trello.post_trello("https://api.trello.com/1/checklists/" + checklists[0]["id"] + "/checkItems/?name=" + title)


def set_card_to_complete(id):
    trello.put_trello("https://api.trello.com/1/cards/" + id + "/?idList=" + doneList)


def complete_checklist_item(id, checklist_id):
    trello.put_trello("https://api.trello.com/1/cards/" + id + "/checkItem/" + checklist_id + "/?state=complete")


def delete_card(id):
    trello.delete_trello("https://api.trello.com/1/cards/" + id + "?")


def delete_checklist_item(id, checklist_id):
    trello.delete_trello("https://api.trello.com/1/cards/" + id + "/checkItem/" + checklist_id + "/?")


def set_card_in_progress(id):
    trello.put_trello("https://api.trello.com/1/cards/" + id + "/?idList=" + doingList)


def get_card_checklist(id):
    todo = trello.get_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
    if todo:
        return todo[0]["checkItems"]
    else:
        trello.post_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
        todo = trello.get_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
        return todo[0]["checkItems"]

