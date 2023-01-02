# Search a node in BST

from BinaryTree.BT_Node import Node
def search(root,key):
    if root:
        if root.val==key:
            return 1
        if root.val<key:
            return search(root.right,key)
        return search(root.left,key)

