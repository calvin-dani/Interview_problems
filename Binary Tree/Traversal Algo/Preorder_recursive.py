import Tree_module as Tree

tree_root = ''
tree_root = Tree.loadTree()
# Tree.createTree()

def printTreeInorder(node):

    if not node:
        return

    
    print("|",node.value, "|")
    printTreeInorder(node.left)
    printTreeInorder(node.right)

printTreeInorder(tree_root)
