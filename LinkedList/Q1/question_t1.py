import generateLinkedList as ll

head = ll.createLinkedList()
ll.printlinked(head)

setLinked = set()

point = head
while point != None:
    nextValue = point.next
    if nextValue.value in setLinked :
        point.next = nextValue.next
    setLinked.add(point.value)
    point = point.next

print(setLinked)
ll.printlinked(head)

