class solution:
    def insertend(self,head,data):
        newnode=Node(data)
        if head is None:
            return newnode
        
        temp=head
        while temp:
            temp=temp.next
        temp.next=newnode
        return head