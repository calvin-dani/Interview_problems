import opcode



def sortStack(stackOne , stackTwo):
    
    
    while(len(stackOne) != 0):
        stackOnePointer = len(stackOne) - 1
        stackTwoPointer = len(stackTwo) - 1
        popStackOne = stackOne.pop()
        stackOnePointer -= 1
        while(True):
            if stackTwoPointer != -1 and stackTwo[stackTwoPointer] > popStackOne:
                popStackTwo = stackTwo.pop()
                stackTwoPointer -= 1
                stackOne.append(popStackTwo)
            elif stackTwoPointer == -1 or stackTwo[stackTwoPointer] < popStackOne:
                stackTwo.append(popStackOne)
                break

if __name__ == '__main__':
    stackOne = [5,7,1,6,3]
    stackTwo = []
    

    while(True):
        opCode = int(input("Enter the operation 1> Push 2>Pop 3> Peek 4>Print 5> Exit :"))
        if opCode == 5:
            break
        if opCode == 1:
            num = int(input("Please enter a number to push"))
            stackOne.append(num)
            sortStack(stackOne,stackTwo)
        if opCode == 2:
            print(stackTwo.pop())
        if opCode == 3:
            print(stackTwo[-1])
        if opCode == 4:
            print(stackOne)
            print(stackTwo)
        