# Python3 program to for tree traversals

# A class that represents an individual node in a
# Binary Tree
from BT_Node import Node
class BTTraversal:
	def printInorder(self,root):
		if root:
			# First recur on left child
			self.printInorder(root.left)
			# then print the data of node
			print(root.val)
			# now recur on right child
			self.printInorder(root.right)

	def printPreOrder(self,root):
		if root:
			print(root.val)
			self.printPreOrder(root.left)
			self.printPreOrder(root.right)

	def printPostOrder(self,root):
		if root:
			self.printPostOrder(root.left)
			self.printPostOrder(root.right)
			print(root.val)



# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	# root.left.left = Node(4)
	# root.left.right = Node(5)

	# Function call
	print("\nInorder traversal of binary tree is")
	bttraversal=BTTraversal()
	bttraversal.printInorder(root)

	# bttraversal.printPostOrder(root)
