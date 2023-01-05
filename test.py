import sys
from BinaryTree.BT_Node import Node
class Solution:
    def isBST(self,root,min,max):
        if root is None: return None
        if min<root.val and root.val<max:
            left=self.isBST(root.left,min,root.val)
            right=self.isBST(root.right,root.val,max)
            return left and right
        else:
            return False
    def isValidBST(self, root):
        max=sys.maxsize
        min=-sys.maxsize-1
        return self.isBST(root,min,max)
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

    solution=Solution()
    a=solution.isValidBST(root)
    print(a)