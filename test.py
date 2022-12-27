from BinaryTree.BT_Node import Node

def printLevelOrder(root):
    if root is None:
        return
    queue=[]
    queue.append(root)
    while len(queue)>0:
        print(queue[0].val,end=" ")
        node=queue.pop(0)
        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)
# Driver Program to test above function
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print("Level Order Traversal of binary tree is -")
printLevelOrder(root)