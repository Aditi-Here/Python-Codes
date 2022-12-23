class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def insertAfter(self,pre_node,new_data):
        if pre_node is None:
            print('Previous node is None.')
            return
        new_node=Node(new_data)
        new_node.next = pre_node.next
        pre_node.next=new_node

