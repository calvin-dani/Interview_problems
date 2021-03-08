import random


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


def createLoopLL():
    num = random.randrange(9)
    head = Node(num)
    point = head
    length = random.randrange(5)
    for i in range(length):
        num = random.randrange(9)
        point.next = Node(num)
        point = point.next

    randomIdx = random.randrange(length)
    loopHead = head

    for i in range(length):
        if i == randomIdx:
            point.next = loopHead
            break
        loopHead = loopHead.next

    return (head, length)


def printlinked(head):
    print("This is the linked List")
    for i in range(10):
        print(head.value)
        head = head.next
    print("This is the end of the linked list")
