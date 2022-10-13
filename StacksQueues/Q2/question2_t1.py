class TripleStack:
    def __init__(self) -> None:
        self.length = 1
        self.mainStack = [None] * self.length
        self.stackIndex = -1
        self.minPointer = -1
        self.minNumber = None

    def resizeStack(self):
        tempLength = self.length * 2
        tempMainStack = [None] * tempLength
        
        for Index in range(self.length):
            tempMainStack[Index] = self.mainStack[Index]

        self.length = tempLength
        self.mainStack = tempMainStack        

    def checkSizeEnough(self):
        if(self.length == sum(self.stackIndex)):
            return False
        return True
    
    def checkIsEmpty(self):
        if self.stackIndex == -1:
            return True
        return False
    
    def checkIsFull(self):
        if(len(self.mainStack) == self.length):
            self.resizeStack()
        return True    

    def updateStackIndexBy(self,changeBy,newEle):
        self.stackIndex += changeBy
        if self.minNumber == None or newEle < self.minNumber :
            self.minNumber = newEle
            self.minPointer = self.stackIndex

    def peekStack(self):
        if self.stackIndex == -1:
            return "Empty stack"
        return self.mainStack[self.stackIndex]
    
    def popStack(self):
        if not self.checkIsEmpty():
            poppedElement = self.mainStack[self.stackIndex]
            self.mainStack[self.stackIndex] = None
            filter = [i for i in self.mainStack if i is not None]
            self.minNumber = None if len(filter)==0 else min(filter)
            if self.minNumber != None:
                self.minPointer = self.mainStack.index(self.minNumber)
            else:
                self.minPointer = -1 
            self.updateStackIndexBy(-1)
            return poppedElement
        else:
            print("Stack is emppty cannot pop any element. Please add to continue")
    
    def pushStack(self, newEle):
        if self.checkIsFull():
            self.mainStack[self.stackIndex+1] = newEle
            self.updateStackIndexBy(1,newEle)
        else:
            print("Stack is full cannot push any element. Please remove to continue")

    def operation(self, stackOp):
        if(stackOp == 1):
            return self.peekStack()
        if(stackOp == 2):
            return self.popStack()
        if(stackOp == 3):
            try:
                newEle  = int(input("Enter the number to enter : "))
            except:
                print("invalid entry")
            else:
                return self.pushStack(newEle)
        if stackOp == 4:
            return self.mainStack[self.minPointer]
        if stackOp == 5:
            print(self.mainStack)

def main():
    stack = TripleStack()

    while True:
        print("Normal STACK with MIN")
        # stackNum = input("Select stack 1 or 2 or 3:")
        operationString = ''' Do you want to
        1) Peek
        2) Pop
        3) Push
        4) Min Number
        5) Print ALL
        6)Exit --> '''
        stackOp = input(operationString)
        
        if stackOp == 6:
            return
        try:
            # stackNum = int(stackNum)
            stackOp = int(stackOp)
            print(stack.operation(stackOp))
        except:
            print("invalid Entry")
        else:
            continue
        






if __name__ == "__main__":
    main()