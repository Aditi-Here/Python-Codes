from BinaryTree.BT_Node import  Node
# def rangeSum(root,low,high):
#     if root is None:
#         return
#     queue=[]
#     queue.append(root)
#     res=[]
#     range_sum=[]
#     while len(queue)>0:
#         node=queue.pop(0)
#         res.append(node.val)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     for i in res:
#         if low<=i<=high:
#             range_sum.append(i)
#     return sum(range_sum)

def rangeSum(root,low,high):
    if root is None:return
    queue=[]
    queue.append(root)
    res=[]
    while len(queue)>0:
        node=queue.pop(0)
        cur=node.val
        if low<=cur<=high:
            res.append(cur)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return sum(res)


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

    res=rangeSum(root,6,10)
    print(res)