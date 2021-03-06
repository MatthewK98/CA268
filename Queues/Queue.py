#
#  Create a queue relying on a Stack. Actually Two Stacks.
#
#  The Stack ADT has three methods:
#     isempty(), push() and pop()
#
from Stack import Stack

class Queue:
    def __init__(self):
        self.enstack = Stack()
        self.destack = Stack()

    def isempty(self):
        return self.enstack.isempty() and self.destack.isempty()

    def enqueue(self, item):
        self.enstack.push(item)

    def dequeue(self):
        if not self.destack.isempty():
            return self.destack.pop()
        while not self.enstack.isempty():
            self.destack.push(self.enstack.pop())
        return self.destack.pop()
