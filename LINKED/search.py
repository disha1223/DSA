class solution:
    def search(self,head,X):
        temp=head
        while temp:
            if temp.val==X:
                return temp
            temp=temp.next
        return None