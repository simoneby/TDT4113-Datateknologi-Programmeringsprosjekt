import unittest
from Queue import*
from Stack import*

class test(unittest.TestCase):

    def test_Queue(self):
        q = Queue()
        q.push(1)
        q.push(4)
        q.push(6)
        q.push(3)
        q.push(2)
        while not (q.is_empty()):
            print(q.pop())
            print(str(q.size()) + " elements left")

    def test_Stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(4)
        stack.push(6)
        stack.push(3)
        stack.push(2)
        while not (stack.is_empty()):
            print(stack.pop())
            print(str(stack.size()) + " elements left")

