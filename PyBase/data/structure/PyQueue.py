# Ref: https://www.programiz.com/dsa/queue
class PyQueue:

    def __init__(self, max_size=10):
        self.queue = []
        self.max_size = max_size

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return self.size() == self.max_size

    def add(self, item):
        self.queue.append(item)

    def remove(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
