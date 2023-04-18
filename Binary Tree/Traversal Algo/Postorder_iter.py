import Tree_module as Tree

tree_root = ''
tree_root = Tree.loadTree()
# Tree.createTree()

def printTreeInorder(node):

    cur = node
    stack = []
    while not (cur is None) or len(stack) > 0:
        # print(stack)
        if not (cur is None):
            # print("IF")
            # print(cur.value)
            stack.append(cur)
            cur = cur.left
        else:
            # print("ELIF")
            # print(stack)
            # cur = stack.pop()
            # print("|",cur.value,"|")
            temp = stack[-1].right
            if (temp is None):
                temp = stack.pop()
                print("|",temp.value,"|")
                while len(stack) > 0 and temp == stack[-1].right:
                    temp = stack.pop()
                    print("|",temp.value,"|")

            else:
                cur = temp
        # print([i.value for i in stack],cur)

printTreeInorder(tree_root)
