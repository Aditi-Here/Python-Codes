class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
if __name__=='__main__':
    root=Node(10)
    root.left=Node(5)
    root.right=Node(12)
    root.left.left=Node(4)
    root.left.right=Node(6)
    root.right.left=Node(11)
