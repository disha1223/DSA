class solution:
    def mid(self,head):
        temp=head
        stack=[]
        while temp:
            stack.append(temp.val)
            temp=temp.next

        temp=head
        while temp:
            temp.data=stack.pop()
            temp=temp.next
        return head