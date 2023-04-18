import Tree_module as Tree

tree_root = ''
tree_root = Tree.loadTree()
# Tree.createTree()

def printTreeInorder(node):

    cur = node
    stack = []
    while cur or len(stack) > 0:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        print("|",cur.value,"|")
        cur = cur.right


printTreeInorder(tree_root)
