class Container:

    def __init__(self):
        self._items = []

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        return self._items.append(item)

    def pop(self):
        assert not self.is_empty()
        raise NotImplementedError

    def peek(self):
        assert not self.is_empty()
        raise NotImplementedError

    def get_items(self):
        return self._items

