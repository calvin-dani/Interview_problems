import generateLinkedList as ll

head = ll.createLinkedList()
ll.printlinked(head)


def traversingNode(head, k):
    if head is None:
        count = 0
        return count + 1

    count = traversingNode(head.next, k)
    if count == k:
        print(head.value)
    return count + 1


traversingNode(head, 3)
