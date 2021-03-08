import generateLinkedList as ll


def checkIfLooped(linkedL):
    head = linkedL
    addressSet = set()
    while head is not None:
        if head not in addressSet:
            addressSet.add(head)
        else:
            return head

        head = head.next


def main():

    integerOne, lengthIntegerOne = ll.createLoopLL()
    ll.printlinked(integerOne)

    val = checkIfLooped(integerOne)
    print("integerOne loop begins at", val, val.value)


main()
