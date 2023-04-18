import Tree_module as Tree

tree_root = ''
tree_root = Tree.loadTree()
# Tree.createTree()

def printTreeInorder(node):

    if not node:
        return

    
    printTreeInorder(node.left)
    print("|",node.value, "|")
    printTreeInorder(node.right)

printTreeInorder(tree_root)
