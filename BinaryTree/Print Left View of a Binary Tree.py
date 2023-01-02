# # Python3 program to print left view of
# # Binary Tree
#
# class newNode:
#
# 	# Construct to create a newNode
# 	def __init__(self, key):
# 		self.data = key
# 		self.left = None
# 		self.right = None
# 		self.hd = 0
#
# def printLeftView(root):
# 	if (not root):
# 		return
# 	q = []
# 	q.append(root)
# 	while (len(q)):
# 		# number of nodes at current level
# 		n = len(q)
# 		# Traverse all nodes of current level
# 		for i in range(1, n + 1):
# 			temp = q[0]
# 			q.pop(0)
#
# 			# Print the left most element
# 			# at the level
# 			if (i == 1):
# 				print(temp.data, end=" ")
#
# 			# Add left node to queue
# 			if (temp.left != None):
# 				q.append(temp.left)
#
# 			# Add right node to queue
# 			if (temp.right != None):
# 				q.append(temp.right)
#
#
# # Driver Code
# if __name__ == '__main__':
#
# 	root = newNode(10)
# 	root.left = newNode(2)
# 	root.right = newNode(3)
# 	root.left.left = newNode(7)
# 	root.left.right = newNode(8)
# 	root.right.right = newNode(15)
# 	root.right.left = newNode(12)
# 	root.right.right.left = newNode(14)
# 	printLeftView(root)
#
#
# Python program to print left view of Binary Tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def leftViewUtil(root, level, max_level,s):
    if root is None:
        return
    if (max_level[0] < level):
        s.append(root.data)
        print(root.data, end=" ")
        max_level[0] = level
    leftViewUtil(root.left, level + 1, max_level,s)
    leftViewUtil(root.right, level + 1, max_level,s)
    return s

def leftView(root):
    max_level = [0]
    s=[]
    l=leftViewUtil(root, 1, max_level,s)
    return l


# Driver program to test above function
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    root.right.right.left = Node(14)

    i=leftView(root)
    print('i: ',i)

