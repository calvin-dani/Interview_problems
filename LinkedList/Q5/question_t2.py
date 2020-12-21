import generateLinkedList as ll

integerOne, lengthIntegerOne = ll.createLinkedList()
ll.printlinked(integerOne)

integerTwo, lengthIntegerTwo = ll.createLinkedList()
ll.printlinked(integerTwo)


def addTheLinked(integerOne, integerTwo, remainder):

    if integerOne is None and integerTwo is None:
        if remainder > 0:
            tail = ll.Node(remainder)
            return tail
        return None

    elif integerOne is None:
        integer1 = 0
        integer2 = integerTwo.value
        sumInteger = integer1 + integer2 + remainder
        remainder = 0
        if sumInteger >= 10:
            remainder = 1
            sumInteger -= 10
        head = ll.Node(sumInteger)
        passRefOne = None
        passRefTwo = integerTwo.next if integerTwo.next is not None else None
        head.next = addTheLinked(passRefOne, passRefTwo, remainder)
        return head

    elif integerTwo is None:
        integer1 = integerOne.value
        integer2 = 0
        sumInteger = integer1 + integer2 + remainder
        remainder = 0
        if sumInteger > 10:
            remainder = 1
            sumInteger -= 10
        head = ll.Node(sumInteger)
        passRefOne = integerOne.next if integerOne.next is not None else None
        passRefTwo = None
        head.next = addTheLinked(passRefOne, passRefTwo, remainder)
        return head

    elif integerOne is not None and integerTwo is not None:
        integer1 = integerOne.value
        integer2 = integerTwo.value
        sumInteger = integer1 + integer2 + remainder
        remainder = 0
        if sumInteger > 10:
            remainder = 1
            sumInteger -= 10
        head = ll.Node(sumInteger)
        passRefOne = integerOne.next if integerOne.next is not None else None
        passRefTwo = integerTwo.next if integerTwo.next is not None else None
        head.next = addTheLinked(passRefOne, passRefTwo, remainder)
        return head


def main():
    headSum = addTheLinked(integerOne, integerTwo, 0)
    ll.printlinked(headSum)
    return headSum


main()
