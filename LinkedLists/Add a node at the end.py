class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head==None:
            self.head=new_node
            return
        else:
            last=self.head
            while (last.next):
                last=last.next
            last.next=new_node


