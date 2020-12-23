import generateLinkedList as ll


def makeThemSame(integerOne, integerTwo, lengthOne, lengthTwo):
    (integerOne, integerTwo) = (
        (integerOne, integerTwo) if lengthOne >= lengthTwo else (integerTwo, integerOne)
    )

    integerTwo = appendZero(integerTwo, abs(lengthOne - lengthTwo))
    return (integerOne, integerTwo)


def appendZero(head, length):

    zeroHead = None

    for num in range(length):
        if zeroHead is None:
            zeroHead = ll.Node(0)
            zeroTail = zeroHead
        else:
            zeroTail.next = ll.Node(0)
            zeroTail = zeroTail.next
    zeroTail.next = head
    head = zeroHead
    return head


def sumLinkedRecRev(integerOne, integerTwo, remainder):

    if integerOne is None or integerTwo is None:
        return (None, 0)

    head = ll.Node(0)
    (head.next, remainder) = sumLinkedRecRev(
        integerOne.next, integerTwo.next, remainder
    )
    sum = integerOne.value + integerTwo.value + remainder
    remainder = 0
    if sum >= 10:
        sum -= 10
        remainder = 1
    head.value = sum
    return (head, remainder)


def main():
    integerOne, lengthIntegerOne = ll.createLinkedList()
    ll.printlinked(integerOne)
    integerTwo, lengthIntegerTwo = ll.createLinkedList()
    ll.printlinked(integerTwo)
    (integerOne, integerTwo) = makeThemSame(
        integerOne, integerTwo, lengthIntegerOne, lengthIntegerTwo
    )
    (head, remainder) = sumLinkedRecRev(integerOne, integerTwo, 0)
    if remainder > 0:
        tempHead = ll.Node(1)
        tempHead.next = head
        head = tempHead
    ll.printlinked(head)
    return head


main()
