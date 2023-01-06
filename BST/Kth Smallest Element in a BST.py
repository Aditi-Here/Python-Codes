from BinaryTree.BT_Node import Node
def kthSmallest(root, k) :
    i = 0
    return helper(root,i,k)

def helper(root, i, k):
    if root is None:
        return None
    left = helper(root.left, i, k)
    if left is not None:
        return left
    if k == (i + 1):
        return root.val
    else:
        return helper(root.right, i + 1, k)
if __name__=='__main__':
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.left.left.left=Node(1)
    a=kthSmallest(root,3)
    print(a)