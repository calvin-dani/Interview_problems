import generateLinkedList as ll

head = ll.createLinkedList()
ll.printlinked(head)

def findKNode(head , k):

    pointer1 = head
    pointer2 = head

    for i in range(k):
        pointer1 = pointer1.next

    while pointer1 != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    print(pointer2.value)

findKNode(head , 3)