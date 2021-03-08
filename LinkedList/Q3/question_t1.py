import generateLinkedList as ll
import random

head, length = ll.createLinkedList()
ll.printlinked(head)


def randomNode(head):
    print(length, "length")
    randomNodeIdx = random.randrange(length)
    print(randomNodeIdx, "randomIdx")
    for i in range(randomNodeIdx):
        head = head.next
    return head


randomIdxNode = randomNode(head)


def deleteRandomNode(pointer1, pointer2):
    while pointer2.next is not None:
        pointer1.value = pointer2.value
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    pointer1.next = None


deleteRandomNode(randomIdxNode, randomIdxNode.next)
ll.printlinked(head)