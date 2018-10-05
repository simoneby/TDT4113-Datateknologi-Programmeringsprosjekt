from Container import*

class Stack(Container):

    def __init__(self):
        super(Stack, self).__init__()

    def peek(self):
        return self._items[-1]

    def pop(self):
        return self._items.pop(-1)
