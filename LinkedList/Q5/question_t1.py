import generateLinkedList as ll

integerOne, lengthIntegerOne = ll.createLinkedList()
ll.printlinked(integerOne)

integerTwo, lengthIntegerTwo = ll.createLinkedList()
ll.printlinked(integerTwo)


def convertToInteger(head):
    integerStrArr = []
    integerStr = ""
    while head is not None:
        integerStrArr.append(str(head.value))
        head = head.next

    integerStrArr.reverse()
    integerStr = "".join(integerStrArr)
    integer = int(integerStr)
    return integer


def convertToLinkedList(integer):
    integerStr = str(integer)
    head = None
    for letter in integerStr:
        if head is None:
            head = ll.Node(int(letter))
        else:
            temp = ll.Node(int(letter))
            temp.next = head
            head = temp
    return head


def main():
    integer1 = convertToInteger(integerOne)
    integer2 = convertToInteger(integerTwo)
    head = convertToLinkedList(integer1 + integer2)
    ll.printlinked(head)
    return head


main()
