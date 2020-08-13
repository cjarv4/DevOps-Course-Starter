from flask import session
import os
import requests

# debug = True
debug = False


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    cards, doing, done = get_cards()

    if debug:
        print("cards - ")
        print(cards)
        print("boards - ")
        get_boards()
        print("lists - ")
        get_lists()
    return cards, doing, done


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items, doing, done = get_items()
    items = items + doing + done
    return next((item for item in items if item['id'] == id), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    # items = get_items()

    # Determine the ID for the item based on that of the previously added item
    # item = create_new_item(items[-1]['id'] + 1 if items else 0, title)

    post_trello("https://api.trello.com/1/cards?idList=5f3169df33611522761de7cc&name=" + title)
    # Add the item to the list
    # items.append(item)
    # session['items'] = items

    # return item


# https://api.trello.com/1/lists/5f3169df33611522761de7cc/cards?token=0ee7c15267a7a7fee3f90ebed124aa5e14652888ce7fc40b444ab7b9ebcbd019&key=d3cfc4a193b13c194d0ca2484808d1f2

def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item


def delete_item(id):
    # existing_items = get_items()
    # existing_items.remove(item)
    # updated_items = existing_items
    #
    # session['items'] = updated_items
    delete_trello("https://api.trello.com/1/cards/" + id + "?")


def complete_item(id):
    put_trello("https://api.trello.com/1/cards/" + id + "/?idList=5f3169dff5e94e5d22ec1d0f")


def complete_checklist_item(id,checklist_id):
    put_trello("https://api.trello.com/1/cards/" + id + "/checkItem/"+checklist_id+"/?state=complete")


def delete_checklist_item(id,checklist_id):
    delete_trello("https://api.trello.com/1/cards/" + id + "/checkItem/"+checklist_id+"/?")


def create_new_item(id, title, status='Not Started'):
    item = {'id': id, 'title': title, 'status': status}
    return item


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
    # doing = get_trello("https://api.trello.com/1/lists/5f3169e0916e3156fd3d1680/cards?fields=id,closed,name")
    # done = get_trellxo("https://api.trello.com/1/lists/5f3169dff5e94e5d22ec1d0f/cards?fields=id,closed,name")
    # print("printing todo")
    print(todo)
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
    print(url)
    print(response)
    return response


def delete_trello(url):
    url = add_trello_token_and_key(url)
    response = requests.delete(url=url)
    return response


def add_trello_token_and_key(url):
    return url + "&token=" + os.getenv(
        'TRELLO_TOKEN') + "&key=" + os.getenv('TRELLO_KEY')
