import generateLinkedList as ll


def findIntersection(integerOne, integerTwo, lengthOne, lengthTwo):

    addressSet = set()

    while integerOne is not None:
        addressSet.add(integerOne)
        integerOne = integerOne.next

    while integerTwo is not None:
        if integerTwo in addressSet:
            return integerTwo
        integerTwo = integerTwo.next


def main():

    integerOne, lengthIntegerOne = ll.createLinkedList()
    ll.printlinked(integerOne)

    integerTwo, lengthIntegerTwo = ll.createDaIntersection(integerOne)
    ll.printlinked(integerTwo)

    lengthIntegerTwo += lengthIntegerOne

    intersectionNode = findIntersection(
        integerOne, integerTwo, lengthIntegerOne, lengthIntegerTwo
    )
    print(
        "the interstion Node is ",
        intersectionNode,
        "and its value is ",
        intersectionNode.value,
    )


main()
