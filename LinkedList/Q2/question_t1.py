import generateLinkedList as ll

head = ll.createLinkedList()
ll.printlinked(head)

def findLength(head):
    point = head
    number = 0
    while point != None:
        number += 1
        point = point.next

    print(number)
    return number

def kAddNode(head ,number , k):
    point = head
    index = number - k
    number = 0
    while point != None:
        number += 1
        point = point.next
        if number == index:
            return point.value

number = findLength(head)

print(kAddNode(head, number , 3))


    
    

