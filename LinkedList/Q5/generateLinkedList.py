import random


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


def createLinkedList():
    head = Node(7)
    point = head
    length = random.randrange(5)
    for i in range(length):
        point.next = Node(random.randrange(9))
        point = point.next
    return (head, length)


def printlinked(head):
    print("This is the linked List")
    while head is not None:
        print(head.value)
        head = head.next
    print("This is the end of the linked list")
