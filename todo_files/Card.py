import trello as trello

toDoListId = trello.get_trello_list_id("To Do")
doingListId = trello.get_trello_list_id("Doing")
doneListId = trello.get_trello_list_id("Done")


class Card:
    def __init__(self, id, name, desc, due, last_activity):
        self.id = id
        self.name = name
        self.desc = desc
        self.due = due
        self.last_activity = last_activity


def get_cards():
    todo = trello.get_trello("lists/" + toDoListId + "/cards?")
    doing = trello.get_trello("lists/" + doingListId + "/cards?")
    done = trello.get_trello("lists/" + doneListId + "/cards?")

    return convertToArrayOfCards(todo), convertToArrayOfCards(doing), convertToArrayOfCards(done)


def get_all_cards():
    todo, doing, done = get_cards()
    return todo + doing + done


def convertToArrayOfCards(items):
    returnList = []
    for item in items:
        newItem = convertToCard(item)
        returnList.append(newItem)
    return returnList


def convertToCard(item):
    return Card(item["id"], item["name"], item["desc"], item["due"], item["dateLastActivity"])


def get_card_by_id(id):
    card = next((card for card in get_all_cards() if card.id == id), None)
    return trim_timestamp(card)


def get_card_by_name(name):
    card = next((card for card in get_all_cards() if card.name == name), None)
    return trim_timestamp(card)


def trim_timestamp(card):
    if card.due:
        card.due = card.due[0:10]  # ignore timestamp
    return card


def add_card(title, desc, dueDate):
    trello.post_trello(
        "cards?idList=" + toDoListId + "&name=" + title + "&desc=" + desc + "&due=" + dueDate)


def add_checklist_item(id, title):
    checklists = trello.get_trello("cards/" + id + "/checklists?")
    trello.post_trello("checklists/" + checklists[0]["id"] + "/checkItems/?name=" + title)


def set_card_to_complete(id):
    trello.put_trello("cards/" + id + "/?idList=" + doneListId)


def complete_checklist_item(id, checklist_id):
    trello.put_trello("cards/" + id + "/checkItem/" + checklist_id + "/?state=complete")


def delete_card(id):
    trello.delete_trello("cards/" + id + "?")


def delete_checklist_item(id, checklist_id):
    trello.delete_trello("cards/" + id + "/checkItem/" + checklist_id + "/?")


def set_card_in_progress(id):
    trello.put_trello("cards/" + id + "/?idList=" + doingListId)


def get_card_checklist(id):
    todo = trello.get_trello("cards/" + id + "/checklists?")
    if todo:
        return todo[0]["checkItems"]
    else:
        trello.post_trello("cards/" + id + "/checklists?")
        todo = trello.get_trello("cards/" + id + "/checklists?")
        return todo[0]["checkItems"]
