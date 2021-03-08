import generateLinkedList as ll


def checkIntersection(integerOne, integerTwo):
    pointerOne = integerOne
    while pointerOne.next is not None:
        pointerOne = pointerOne.next

    pointerTwo = integerTwo
    while pointerTwo.next is not None:
        pointerTwo = pointerTwo.next
    return pointerOne is pointerTwo


def findIntersection(integerOne, integerTwo, lengthOne, lengthTwo):
    if lengthTwo > lengthOne:
        (integerOne, integerTwo) = (integerTwo, integerOne)
        (lengthOne, lengthTwo) = (lengthTwo, lengthOne)

    for i in range(lengthOne - lengthTwo):
        integerOne = integerOne.next

    while integerOne is not None:
        if integerOne is integerTwo:
            print(integerOne.value)
            return integerOne
        integerOne = integerOne.next
        integerTwo = integerTwo.next


def main():

    integerOne, lengthIntegerOne = ll.createLinkedList()
    ll.printlinked(integerOne)

    integerTwo, lengthIntegerTwo = ll.createDaIntersection(integerOne)
    ll.printlinked(integerTwo)

    lengthIntegerTwo += lengthIntegerOne

    if checkIntersection(integerOne, integerTwo):
        intersectionNode = findIntersection(
            integerOne, integerTwo, lengthIntegerOne, lengthIntegerTwo
        )
        print(
            "the interstion Node is ",
            intersectionNode,
            "and its value is ",
            intersectionNode.value,
        )
        quit()
    print("intersection doesnt exist :)")


main()
