import Card as card


class ViewModel:
    def __init__(self, todo, doing, done, show_all):
        self._todo = todo
        self._doing = doing
        self._done = done
        self._show_all = show_all

    @property
    def todo(self):
        return self._todo

    @property
    def doing(self):
        return self._doing

    @property
    def done(self):
        if len(self._done) < 5 or self._show_all:
            return self._done
        else:
            return card.get_complete_items_from_today(self._done)
