import generateLinkedList as ll

head = ll.createLinkedList()
ll.printlinked(head)


point = head
while point is not None:
    point2 = point.next
    preValue = point
    while point2 is not None:
        if point2.value == point.value:
            preValue.next = point2.next
            point2 = point2.next
            continue
        point2 = point2.next
        preValue = preValue.next
    point = point.next


ll.printlinked(head)
