from Container import*

class Queue(Container):

    def __init__(self):
        super(Queue, self).__init__()

    def peek(self):
        #assert not self.is_empty()
        return self._items[0]

    def pop(self):
        #assert not self.is_empty()
        return self._items.pop(0)
