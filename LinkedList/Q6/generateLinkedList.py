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
    return (head, length + 1)


def createPalindromeLL():
    num = random.randrange(9)
    head = Node(num)
    head2 = Node(num)
    point = head
    point2 = head2
    length = random.randrange(5)
    for i in range(length):
        num = random.randrange(9)
        point.next = Node(num)
        point = point.next
        temp = Node(num)
        temp.next = point2
        point2 = temp
    point.next = point2
    return (head, ((length + 1) * 2))


def printlinked(head):
    print("This is the linked List")
    while head is not None:
        print(head.value)
        head = head.next
    print("This is the end of the linked list")
