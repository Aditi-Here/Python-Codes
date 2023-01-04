from BinaryTree.BT_Node import Node
def minValue(root):
    if root is None:
        return
    temp=root
    while temp.left!=None:
        temp=temp.left
    return temp.val
if __name__=='__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(13)
    root.right.right = Node(18)
    root.left.left=Node(3)
    root.left.right=Node(7)
    root.left.right.left = Node(6)
    root.left.left.left = Node(1)
    min_value=minValue(root)
    print(min_value)