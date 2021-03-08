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


def createDaIntersection(intersectHead):
    num = random.randrange(9)
    head = Node(num)
    point = head
    length = random.randrange(5)
    randIdx = random.randrange(length)
    for i in range(length):
        if i == randIdx:
            point.next = intersectHead
            break
        num = random.randrange(9)
        point.next = Node(num)
        point = point.next

    return (head, randIdx + 1)


def printlinked(head):
    print("This is the linked List")
    while head is not None:
        print(head.value)
        head = head.next
    print("This is the end of the linked list")
