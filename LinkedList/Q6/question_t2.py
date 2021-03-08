import generateLinkedList as ll


def checkIfPalindrome(linkedL):
    head = linkedL
    linkedStack = []
    while head is not None:
        linkedStack.append(head.value)
        head = head.next

    return linkedStack == linkedStack[::-1]


def main():

    integerOne, lengthIntegerOne = ll.createLinkedList()
    ll.printlinked(integerOne)

    integerTwo, lengthIntegerTwo = ll.createPalindromeLL()
    ll.printlinked(integerTwo)

    val = checkIfPalindrome(integerOne)
    print("integerOne is a Palindrome", val)

    val = checkIfPalindrome(integerTwo)
    print("integerTwo is a palindrome", val)


main()