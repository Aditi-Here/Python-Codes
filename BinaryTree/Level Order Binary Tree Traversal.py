# Python program to print level
# order traversal using Queue

# A node structure


class Node:
	# A utility function to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

# Iterative Method to print the
# height of a binary tree


def printLevelOrder(root):
	if root is None:
		return
	queue = []
	queue.append(root)
	while(len(queue) > 0):
		print(queue[0].data, end = " ")
		node = queue.pop(0)
		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)


# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
printLevelOrder(root)

