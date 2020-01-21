import sys

class Stack:
#
#  Stack ADT has three methods: is_empty, push and pop.
#
   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]


def check_brackets(line):
    stack = Stack()
    for c in line:
        if c == "(":
            stack.push(c)
        elif c == ")":
            if stack.is_empty():
                return False
            else:
                stack.pop()
    if stack.is_empty():
        return True
    else:
        return False
