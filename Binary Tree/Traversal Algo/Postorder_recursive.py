import Tree_module as Tree

tree_root = ''
tree_root = Tree.loadTree()
# Tree.createTree()

def printTreeInorder(node):

    if not node:
        return

    
    printTreeInorder(node.left)
    printTreeInorder(node.right)
    print("|",node.value, "|")

printTreeInorder(tree_root)
