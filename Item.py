import trello as trello

toDoListId = trello.get_trello_list_id("To Do")
doingListId = trello.get_trello_list_id("Doing")
doneListId = trello.get_trello_list_id("Done")


class Item:
    def __init__(self, id, name, desc, due):
        self.id = id
        self.name = name
        self.desc = desc
        self.due = due


def get_cards():
    todo = trello.get_trello("https://api.trello.com/1/lists/" + toDoListId + "/cards?")
    doing = trello.get_trello("https://api.trello.com/1/lists/" + doingListId + "/cards?")
    done = trello.get_trello("https://api.trello.com/1/lists/" + doneListId + "/cards?")

    return convertToArrayOfItems(todo), convertToArrayOfItems(doing), convertToArrayOfItems(done)


def convertToArrayOfItems(items):
    returnList = []
    for item in items:
        newItem = Item(item["id"], item["name"], item["desc"], item["due"])
        returnList.append(newItem)
    return returnList


def get_card(id):
    todo, doing, done = get_cards()
    cards = todo + doing + done
    card = next((card for card in cards if card.id == id), None)

    if card.due:
        card.due = card.due[0:10]  # ignore timestamp
    return card


def add_card(title, desc, dueDate):
    trello.post_trello(
        "https://api.trello.com/1/cards?idList=" + toDoListId + "&name=" + title + "&desc=" + desc + "&due=" + dueDate)


def add_checklist_item(id, title):
    checklists = trello.get_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
    trello.post_trello("https://api.trello.com/1/checklists/" + checklists[0]["id"] + "/checkItems/?name=" + title)


def set_card_to_complete(id):
    trello.put_trello("https://api.trello.com/1/cards/" + id + "/?idList=" + doneListId)


def complete_checklist_item(id, checklist_id):
    trello.put_trello("https://api.trello.com/1/cards/" + id + "/checkItem/" + checklist_id + "/?state=complete")


def delete_card(id):
    trello.delete_trello("https://api.trello.com/1/cards/" + id + "?")


def delete_checklist_item(id, checklist_id):
    trello.delete_trello("https://api.trello.com/1/cards/" + id + "/checkItem/" + checklist_id + "/?")


def set_card_in_progress(id):
    trello.put_trello("https://api.trello.com/1/cards/" + id + "/?idList=" + doingListId)


def get_card_checklist(id):
    todo = trello.get_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
    if todo:
        return todo[0]["checkItems"]
    else:
        trello.post_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
        todo = trello.get_trello("https://api.trello.com/1/cards/" + id + "/checklists?")
        return todo[0]["checkItems"]
