import trello as trello


class Board:
    def __init__(self, id, name):
        self.id = id
        self.name = name

def add_board(name):
    trello.post_trello("boards?name="+name)
    return get_board_by_name(name)

def delete_board(id):
    trello.delete_trello("boards/" + id + "?")


def get_boards():
    boards = trello.get_trello("members/me/boards?")

    return convertToArrayOfBoards(boards)

def get_board_by_id(id):
    board = next((board for board in get_boards() if board.id == id), None)
    return board

    
def get_board_by_name(name):
    board = next((board for board in get_boards() if board.name == name), None)
    return board

def convertToArrayOfBoards(items):
    returnList = []
    for item in items:
        newItem = convertToBoard(item)
        returnList.append(newItem)
    return returnList


def convertToBoard(item):
    new_board = Board(item["id"], item["name"])
    return new_board
