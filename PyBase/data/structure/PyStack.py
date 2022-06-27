
# Ref: https://www.programiz.com/dsa/stack

class PyStack:

    def __init__(self, max_stack_size=10):
        self.stack = []
        self.max_size = max_stack_size

    def setSize(self, size):
        self.max_size = size

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return self.size() == self.max_size

    def push(self, item):
        if self.isFull():
            print('Stack is full')
            return
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
            return
        self.stack.pop()

    def display(self):
        print(self.stack)
