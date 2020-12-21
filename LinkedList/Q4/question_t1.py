import generateLinkedList as ll
import random

head, length = ll.createLinkedList()
ll.printlinked(head)


def partitionLinkedList(head, partition):

    lowerPointer = None
    lowerPointerHead = None
    higherPointer = None
    higherPointerHead = None

    while head is not None:
        if head.value < partition:
            if lowerPointer is None:
                lowerPointer = head
                lowerPointerHead = head
            else:
                lowerPointer.next = head
                lowerPointer = lowerPointer.next

        elif head.value >= partition:
            if higherPointer is None:
                higherPointer = head
                higherPointerHead = head
            else:
                higherPointer.next = head
                higherPointer = higherPointer.next

        head = head.next

    lowerPointer.next = higherPointerHead
    higherPointer.next = None
    return lowerPointerHead


partitionValue = random.randrange(7)
print("This is the partition value", partitionValue)
head = partitionLinkedList(head, partitionValue)
print("This is the partitioned linked list")
ll.printlinked(head)
