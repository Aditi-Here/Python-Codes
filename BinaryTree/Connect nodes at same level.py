# # Iterative program to connect all the adjacent nodes at the same level in a binary tree
# class newnode:
# 	def __init__(self, data):
# 		self.data = data
# 		self.left = self.right = self.nextRight = None
#
# # setting right pointer to next right node
#
# #			 10 ----------> NULL
# #			 / \
# #		 8 --->2 --------> NULL
# #		 /
# #		 3 ----------------> NULL
#
#
# def connect(root):
#
# 	# Base condition
# 	if root is None:
# 		return
#
# 	# Create an empty queue like level order traversal
# 	queue = []
# 	queue.append(root)
# 	while len(queue) != 0:
#
# 		# size indicates no. of nodes at current level
# 		size = len(queue)
#
# 		# for keeping track of previous node
# 		prev = newnode(None)
# 		for i in range(size):
# 			temp = queue.pop(0)
# 			if temp.left:
# 				queue.append(temp.left)
# 			if temp.right:
# 				queue.append(temp.right)
# 			if prev != None:
# 				prev.nextRight = temp
# 				prev = temp
# 		prev.nextRight = None
#
#
# # Driver Code
# if __name__ == '__main__':
#
# 	# Constructed binary tree is
# 	# 10
# 	#	 / \
# 	# 8	 2
# 	# /
# 	# 3
# 	root = newnode(10)
# 	root.left = newnode(8)
# 	root.right = newnode(2)
# 	root.left.left = newnode(3)
#
# 	# Populates nextRight pointer in all nodes
# 	connect(root)
#
# 	# Let us check the values of nextRight pointers
# 	print("Following are populated nextRight",
# 		"pointers in the tree (-1 is printed",
# 		"if there is no nextRight)")
# 	print("nextRight of", root.data, "is ", end="")
# 	if root.nextRight:
# 		print(root.nextRight.data)
# 	else:
# 		print(-1)
# 	print("nextRight of", root.left.data, "is ", end="")
# 	if root.left.nextRight:
# 		print(root.left.nextRight.data)
# 	else:
# 		print(-1)
# 	print("nextRight of", root.right.data, "is ", end="")
# 	if root.right.nextRight:
# 		print(root.right.nextRight.data)
# 	else:
# 		print(-1)
# 	print("nextRight of", root.left.left.data, "is ", end="")
# 	if root.left.left.nextRight:
# 		print(root.left.left.nextRight.data)
# 	else:
# 		print(-1)
#


#  Populating Next Right Pointers in Each Node
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None
        queue=[]
        queue.append(root)
        queue.append(None)
        while len(queue)>0:
            node=queue.pop(0)
            if node is not None:
                node.next=queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            elif len(queue)>0:
                queue.append(None)
        return root