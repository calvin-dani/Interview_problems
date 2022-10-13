class StackPlates:
    def __init__(self, sizeOfStack) -> None:
        self.length = 1
        self.stackMaxSize = sizeOfStack
        self.numberOfElements = 0
        self.stackIndex = -1
        self.plateIndex = 0
        self.mainStack = [[None] * sizeOfStack]        

    def resizeStack(self):        
        self.mainStack.append([None]*self.stackMaxSize)
        self.plateIndex += 1

    def checkSizeEnough(self):
        if(self.length == sum(self.stackIndex)):
            return False
        return True
    
    def checkIsEmpty(self):
        return self.numberOfElements == 0
    
    def checkIsFull(self):
        if(self.stackIndex == self.stackMaxSize - 1):
            self.resizeStack()
        return True    

    def updateStackIndexBy(self,changeBy):
        self.numberOfElements += changeBy

    def peekStack(self):
        if self.getStackOrder()-1 == -1:
            return "Empty stack"
        return self.mainStack[self.getPlateOrder()][self.getStackOrder()-1]
    
    def popStack(self):
        if not self.checkIsEmpty():
            print("stack index",self.stackIndex)
            poppedElement = self.mainStack[self.plateIndex][self.stackIndex]
            self.mainStack[self.plateIndex][self.stackIndex] = None
            self.stackIndex = self.stackMaxSize-1 if self.stackIndex -1 == -1 else self.stackIndex - 1
            self.updateStackIndexBy(-1)
            if self.stackIndex == self.stackMaxSize-1 :
                self.mainStack.pop()
                self.plateIndex += -1
            return poppedElement
        else:
            print("Stack is emppty cannot pop any element. Please add to continue")
    
    def pushStack(self, newEle):
        if self.checkIsFull():
            self.stackIndex = (self.stackIndex +1) % self.stackMaxSize
            print("plat",self.plateIndex)
            self.mainStack[self.plateIndex][self.stackIndex] = newEle
            self.updateStackIndexBy(1)
            
        else:
            print("Stack is full cannot push any element. Please remove to continue")
    
    def getStackOrder(self):
        return self.numberOfElements % self.stackMaxSize 
    
    def getPlateOrder(self):
        platOrd = self.numberOfElements // self.stackMaxSize 
        return platOrd-1 if self.numberOfElements % self.stackMaxSize == 0 else  platOrd

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
            print(self.mainStack)

def main():
    sizeOfStack = int(input("Enter the max size of stack: "))
    plateStack = StackPlates(sizeOfStack)

    while True:
        print("Normal STACK with PLATES")
        # stackNum = input("Select stack 1 or 2 or 3:")
        operationString = ''' Do you want to
        1) Peek
        2) Pop
        3) Push
        4) Print ALL
        5)Exit --> '''
        stackOp = input(operationString)
        
        if stackOp == 6:
            return
        try:
            # stackNum = int(stackNum)
            stackOp = int(stackOp)
            print(plateStack.operation(stackOp))
        except:
            print("invalid Entry")
        else:
            continue


if __name__ == '__main__':
    main()