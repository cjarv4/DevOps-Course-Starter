class ViewModel:
    def __init__(self, todo, doing, done):
        self._todo = todo
        self._doing = doing
        self._done = done

    @property
    def todo(self):
        return self._todo

    @property
    def doing(self):
        return self._doing

    @property
    def done(self):
        return self._done