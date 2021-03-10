import generateLinkedList as ll


def checkIfLooped(linkedL):
    pointerOne = linkedL
    pointerTwo = linkedL.next

    while not pointerOne is pointerTwo:
        pointerOne = pointerOne.next
        pointerTwo = pointerTwo.next.next

    return pointerTwo.next


def main():

    integerOne, lengthIntegerOne = ll.createLoopLL()
    ll.printlinked(integerOne)

    val = checkIfLooped(integerOne)
    print("integerOne loop begins at", val, val.value)


main()
