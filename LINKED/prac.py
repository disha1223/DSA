class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked:
    def __init__(self):
        self.head=None

    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
            


l1=linked()
l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
l1.display()