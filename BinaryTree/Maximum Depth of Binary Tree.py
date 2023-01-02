from BT_Node import Node
def maxDepth(root):
    if root is None:
        return 0
    else:
        rDepth = maxDepth(root.right)
        lDepth = maxDepth(root.left)
        if rDepth > lDepth:
            return rDepth + 1
        else:
            return lDepth + 1

if __name__=="__main__":
    root=Node(1)
    root.left = Node(2)
    root.right = Node(3)
    arr=maxDepth(root)
    print(arr)