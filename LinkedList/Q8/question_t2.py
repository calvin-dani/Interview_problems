import generateLinkedList as ll


def checkIfLooped(linkedL):
    pointerOne = linkedL
    pointerTwo = linkedL.next

    while not (pointerOne is pointerTwo) and pointerTwo is not None:
        pointerOne = pointerOne.next
        pointerTwo = pointerTwo.next.next

    lengthOfCycle = 0
    if pointerOne is pointerTwo:
        pointerOne = pointerOne.next
        lengthOfCycle = 1
        while pointerOne is not pointerTwo:
            pointerOne = pointerOne.next
            lengthOfCycle += 1

    return (True,lengthOfCycle) if pointerTwo is pointerOne else (False,lengthOfCycle)

def checkCycleStart(linkedL,lengthOfCycle):
    pointerOne = linkedL
    pointerTwo = linkedL
    for step in range(lengthOfCycle):
        pointerTwo = pointerTwo.next
    
    while pointerOne is not pointerTwo:
        pointerOne = pointerOne.next
        pointerTwo = pointerTwo.next

    return pointerOne
        



def main():

    integerOne, lengthIntegerOne = ll.createLoopLL()
    ll.printlinked(integerOne)

    checkLoop,lengthOfCycle = checkIfLooped(integerOne)
    if checkLoop:
        val = checkCycleStart(integerOne,lengthOfCycle)
        print("integerOne loop begins at", val, val.value)
    print("This linked list is acyclic")

main()
