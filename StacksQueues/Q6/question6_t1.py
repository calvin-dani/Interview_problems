import opcode
from time import time

from datetime import datetime

class Animal:
    def __init__(self,name,animal) -> None:
        self.name = name
        self.timeStamp = datetime.now()
        self.animal = animal[0]

if __name__ == '__main__':
    dawgStack = []
    catoStack = []
    while(True):
        actionCode = int(input("1> Adopt or 2> donate :"))
        if actionCode == 2:
            opCode = int(input("U wanna 1> dawg or 2> cato :"))
            if opCode == 1:
                newDawg = Animal(input("Enter dawg name :"),"DOG")
                dawgStack.append(newDawg)
            if opCode == 2:
                newCato = Animal(input("Enter cato name :"),"CAT")
                catoStack.append(newCato)
        elif actionCode == 1:
            opCode = int(input("U wanna 1> dawg or 2> cato or 3> any :"))
            if opCode == 1:
                if len(dawgStack) > 0:
                     print(dawgStack.pop(0).name)
                else:
                    print("no dawgs")
            if opCode == 2:
                if len(catoStack) > 0:
                     print(catoStack.pop(0).name)
                else:
                    print("no cato")
            if opCode ==3:
                if len(catoStack) > 0 and len(dawgStack) > 0:
                    print(catoStack.pop(0).name if catoStack[0].timeStamp < dawgStack[0].timeStamp else dawgStack.pop(0).name)
                elif len(dawgStack) == 0:
                    print(catoStack.pop(0).name)
                elif len(catoStack) == 0:
                    print(dawgStack.pop(0).name)

                

