# Ref: Singly Linked List
#     -   https://www.programiz.com/dsa/linked-list
#     -   https://www.programiz.com/dsa/linked-list-operations

import logging


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def setData(self, data):
        self.item = data

    def getData(self):
        return self.item

    def next(self):
        return  self.next


class PyLinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert after a node
    def insertAfter(self, prev_node, data):
        if prev_node is None:
            logging.warn('The given previous node must in LinkedList.')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # Deleting a node
    def deleteNode(self, position):
        if self.head is None:
            return

        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return

        if temp.next is None:
            return

        nextNode = temp.next.next
        temp.next = None
        temp.next = nextNode

    # Search an element
    def search(self, key):
        current = self.head
        while current is not None:
            if current.getData() == key:
                return True
            current = current.next
        return False

    # Sort the linked list
    def sortLinkedList(self, head):
        current = head
        index = Node(None)
        if head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current
                index = current.next
                while index is not None:
                    if current.getData() > index.getData():
                        current.setData(index.getData())
                        index.setData(current.getData())
                    index = index.next
                current = current.next

    def display(self):
        temp = self.head
        while temp:
            print(str(temp.getData()) + " -> ", end="")
            temp = temp.next
