import sys

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these functions are called methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None
    
    def count(self):
    	pointer = self.head
    	count = 0
    	while pointer != None:
    		count += 1
    		pointer = pointer.next
    	i += 1
    
    def contains(self, num):
    	pointer = self.head
    	while pointer != None:
    		if pointer.item == num:
    			return True
    		pointer = pointer.next
    	return False
    
    def after(self, num):
        pointer = self.head
        while pointer and pointer.item != num:
            pointer = pointer.next
        return pointer.next.item if pointer else None
    
    def before(self, num):
        previous = None
        pointer = self.head
        while pointer and pointer.item != num:
            previous = pointer.item
            pointer = pointer.next
        return previous if pointer else None