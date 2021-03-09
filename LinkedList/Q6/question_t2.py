import generateLinkedList as ll


def setRightPointer(pointer, length):
    if length % 2 == 0:
        return pointer.next
    else:
        return pointer.next.next


def checkIfPalindrome(linkedL, lengthL, count):

    if count == lengthL // 2:

        leftP = linkedL
        rightP = setRightPointer(leftP, lengthL)

        if leftP.value == rightP.value:
            return rightP.next
        else:
            return False

    retValue = checkIfPalindrome(linkedL.next, lengthL, count + 1)

    if type(retValue) == bool:
        return False

    leftP = linkedL
    rightP = retValue
    if leftP.value == rightP.value:
        return rightP.next
    else:
        return False


def main():

    integerOne, lengthIntegerOne = ll.createLinkedList()
    ll.printlinked(integerOne)

    integerTwo, lengthIntegerTwo = ll.createPalindromeLL()
    ll.printlinked(integerTwo)

    val = checkIfPalindrome(integerOne, lengthIntegerOne, 1)

    if type(val) != bool:
        print("integerOne is a Palindrome", val)
    else:
        print("integerOne is not a Palindrome")

    val = checkIfPalindrome(integerTwo, lengthIntegerTwo, 1)
    if type(val) != bool:
        print("integerTwo is a Palindrome")
    else:
        print("integerTwo is not a Palindrome")


main()