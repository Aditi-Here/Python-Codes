from BinaryTree.BT_Node import Node

def largestVal(root):
    if root is None:
        return None
    queue=[]
    q=[]
    queue.append(root)
    n=0
    while len(queue)>0:
        q.append(queue[0].val)
        node=queue.pop(0)
        n+=1
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    print('n:',n)
    return q



if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    root.right.right.left = Node(14)

    large_val=largestVal(root)
    print(large_val)


