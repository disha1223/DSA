class solution:
    def rev(self,head):
        temp=head
        prev=None
        while temp:
            front=head.next 
            temp.next=prev #reverselink
            prev=temp
            temp=front
        return prev
