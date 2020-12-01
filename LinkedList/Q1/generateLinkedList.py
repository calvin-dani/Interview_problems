import random


class Node:
    
    def __init__(self,data):
        self.value = data
        self.next = None


def createLinkedList():
    head = Node(7)
    point = head
    for i in range(random.randrange(17)):
        point.next = Node(random.randrange(7))
        point = point.next
    return head

def printlinked(head):
    print("This is the linked List")
    while head!= None:
        print(head.value)
        head = head.next
    print("This is the end of the linked list")

