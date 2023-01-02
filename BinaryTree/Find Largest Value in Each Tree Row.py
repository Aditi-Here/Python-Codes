# # using level order traversal
# from BinaryTree.BT_Node import  Node
# def printLargestValueInLevelOrder(root):
#    if root is None:
#       return
#    queue=[]
#    queue.append([root, 0])
#    s = []
#    ret = []
#    largeVal = []
#    while len(queue) > 0:
#        cur = queue[0][0]
#        h = queue[0][1]
#        queue = queue[1:]
#        if h not in s:
#            s.append(h)
#            ret.append(cur.val)
#        else:
#            ret[h]=max(ret[h],cur.val)
#        if cur.left is not None:
#            queue.append([cur.left, h + 1])
#        if cur.right is not None:
#            queue.append([cur.right, h + 1])
#    print(s)
#    return ret
#
#
# if __name__=="__main__":
#     root=Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.right.left = Node(6)
#     root.left.right = Node(5)
#     root.right.right = Node(7)
#     r=printLargestValueInLevelOrder(root)
#     print(r)
#
#  Using recursion
def helper(res, root, d):
    if (not root):
        return
    if (d == len(res)):
        res.append(root.val)
    else:
        res[d] = max(res[d], root.val)

    helper(res, root.left, d + 1)
    helper(res, root.right, d + 1)

def largestValues(root):
    res = []
    helper(res, root, 0)
    return res

class newNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


# Driver Code
if __name__ == '__main__':
    root = newNode(4)
    root.left = newNode(9)
    root.right = newNode(2)
    root.left.left = newNode(3)
    root.left.right = newNode(5)
    root.right.right = newNode(7)
    print(*largestValues(root))


