from BinaryTree.BT_Node import  Node

def rightside(root):
    queue = []
    if root is None:
        return []
    queue.append([root, 0])
    s = set()
    ret = []
    largeVal=[]
    while len(queue) > 0:
        cur = queue[0][0]
        h = queue[0][1]
        queue = queue[1:]
        ret.append([cur.val,h])
        if cur.left is not None:
            queue.append([cur.left, h + 1])
        if cur.right is not None:
            queue.append([cur.right, h + 1])


    return ret

def largeValue(array):
    h = array[0][1]
    for i in range(1,len(array)):
        h_=array[i][1]
        if h<

if __name__=="__main__":
    root=Node(1)
    root.left = Node(2)
    root.right = Node(3)
    # root.left.left = Node(4)
    # root.right.left = Node(6)
    # root.left.right = Node(5)
    # root.right.right = Node(7)
    right_side=rightside(root)
    print(right_side)
    largeValue(right_side)


