import Tree_module as Tree

tree_root = ''
tree_root = Tree.loadTree()
# Tree.createTree()

def printTreeInorder(node):

    cur = node
    stack = [node]
    # print([i.value for i in stack],'Stack')
    while len(stack) > 0:
        # print([i.value for i in stack],'Stack')
        cur = stack.pop()
        print("|",cur.value,"|")
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            # print("CurL",cur.left.value)
            stack.append(cur.left)
        

printTreeInorder(tree_root)
