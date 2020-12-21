import generateLinkedList as ll

integerOne, lengthIntegerOne = ll.createLinkedList()
ll.printlinked(integerOne)

integerTwo, lengthIntegerTwo = ll.createLinkedList()
ll.printlinked(integerTwo)


def getSummation(valOne, valTwo, remainder):
    sumVal = valOne + valTwo + remainder
    remainder = 0
    if sumVal > 10:
        remainder = 1
        sumVal -= 10
    return (sumVal, remainder)


def addLinkedList(integerOne, integerTwo):
    remainder = 0
    sumHead = None
    while integerOne is not None and integerTwo is not None:
        integer1 = integerOne.value
        integer2 = integerTwo.value
        (sumVal, remainder) = getSummation(integer1, integer2, remainder)
        if sumHead is None:
            sumHead = ll.Node(sumVal)
            tailNode = sumHead
        else:
            tailNode.next = ll.Node(sumVal)
            tailNode = tailNode.next
        integerOne = integerOne.next
        integerTwo = integerTwo.next

    remainingNode = integerOne if integerOne is not None else integerTwo

    while remainingNode is not None:
        integer = remainingNode.value
        (sumVal, remainder) = getSummation(integer, 0, remainder)
        tailNode.next = ll.Node(sumVal)
        tailNode = tailNode.next
        remainingNode = remainingNode.next

    if remainder > 0:
        tailNode.next = ll.Node(remainder)
        tailNode = tailNode.next

    return sumHead


def main():
    head = addLinkedList(integerOne, integerTwo)
    ll.printlinked(head)
    return head


main()
