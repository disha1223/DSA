class solution:
    def insertbeg(self,head,data):
        newnode=Node(data)
        newnode.nbext=head
        head=newnode