class TripleStack:
    def __init__(self) -> None:
        self.length = 3
        self.subLength = 1
        self.mainStack = [None] * self.length
        self.stackBoundaryIndex = [0,1,2]
        self.stackIndex = [-1,0,1]
        self.firstStackLength = 1
        self.secondStackLength = 1
        self.thirdStackLength = 1

    def resizeStack(self):
        tempLength = self.length * 2
        tempSubLength = tempLength / 3
        tempMainStack = [None] * tempLength
        
        oldIndex = 0
        newIndex = 0
        for subIndex in range(self.subLength):
            tempMainStack[newIndex + subIndex] = self.mainStack[oldIndex + subIndex]
        oldIndex += self.subLength
        newIndex += tempSubLength

        self.length = tempLength
        self.subLength = tempSubLength
        self.mainStack = tempMainStack        


    def getStackIndex(self,stackNum):
        if not (stackNum > 3 or stackNum < 1):
            return self.stackIndex[stackNum-1]

    def checkSizeEnough(self):
        if(self.length == sum(self.stackIndex)):
            return False
        return True
    
    def checkIsEmpty(self,stackNum):
        if(self.stackIndex[stackNum-1] <= self.stackBoundaryIndex[stackNum-2]):
            return False
        return True
    
    def checkIsFull(self,stackNum):
        if(self.stackIndex[stackNum-1] >= self.stackBoundaryIndex[stackNum-1]):
            self.resizeStack()
        return True    

    def updateStackIndexBy(self,changeBy,stackNum):
        if not (stackNum > 3 or stackNum < 1):
            self.stackIndex[stackNum - 1] += changeBy

    def peekStack(self,stackNum):
        index = self.getStackIndex(stackNum)
        return self.mainStack[index]
    
    def popStack(self,stackNum):
        if self.checkIsEmpty(stackNum):
            poppedElement = self.mainStack[self.getStackIndex(stackNum)]
            self.updateStackIndexBy(-1,stackNum)
            return poppedElement
        else:
            print("Stack is emppty cannot pop any element. Please add to continue")
    
    def pushStack(self,stackNum, newEle):
        if self.checkIsFull(stackNum):
            self.mainStack[self.getStackIndex(stackNum)+1] = newEle
            self.updateStackIndexBy(1,stackNum)
        else:
            print("Stack is full cannot push any element. Please remove to continue")

    def operation(self,stackNum, stackOp):
        if(stackOp == 1):
            return self.peekStack(stackNum)
        if(stackOp == 2):
            return self.popStack(stackNum)
        if(stackOp == 3):
            try:
                newEle  = int(input("Enter the number to enter : "))
            except:
                print("invalid entry")
            else:
                return self.pushStack(stackNum,newEle)
            
        if stackOp == 4:
            print(self.mainStack)

def main():
    stack = TripleStack()

    while True:
        print("TRIPLE STACK")
        stackNum = input("Select stack 1 or 2 or 3:")
        operationString = ''' Do you want to
        1) Peek
        2) Pop
        3) Push
        4) Print ALL
        5)Exit --> '''
        stackOp = input(operationString)
        
        try:
            stackNum = int(stackNum)
            stackOp = int(stackOp)
            print(stack.operation(stackNum,stackOp))
        except:
            print("invalid Entry")
        else:
            continue
        
        if stackOp == 5:
            break






if __name__ == "__main__":
    main()