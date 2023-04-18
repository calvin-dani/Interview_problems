import pickle
import random
import json
import jsonpickle

class Node:

    def __init__(self) -> None:
        self.value = random.randint(1,10)
        print(self.value)
        self.right = None
        self.left = None

class Tree:

    def __init__(self,root) -> None:
        self.root = root

    def randomInsert(self,number_of_nodes):
        tempNode = self.root
        leftInsert = False
        rightInsert = False
        for _ in range(number_of_nodes):
            if (random.randint(1,10) > 5 and not rightInsert) or leftInsert:
                print("R")
                tempNode.right = Node()
                rightInsert = True
            else:
                print("L")
                tempNode.left = Node()
                leftInsert = True
            
            if leftInsert and rightInsert:
                if random.randint(1,10) > 5:
                    print("RM")
                    tempNode = tempNode.right
                else:
                    print("LM")
                    tempNode = tempNode.left
                leftInsert = False
                rightInsert = False

    def stringfyTree(self):
        with open("tree", 'wb') as outp:  # Overwrites any existing file.
            pickle.dump(self.root, outp, pickle.HIGHEST_PROTOCOL)
        
    
    
def loadTree():
        tree_root = None
        with open('tree','rb') as f:
            tree_root = pickle.load(f)
        return tree_root

def createTree():
    root = Node()
    tree_root = Tree(root)
    tree_root.randomInsert(10)
    tree_root.stringfyTree()