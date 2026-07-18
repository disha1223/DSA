class solution:
    def pali(self,head):
        slow=head
        fast=head
        if head is None or head.next is None:
            return True
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next


            prev=None
            curr=slow.next

            while curr:
                front=curr.next
                curr.next=prev
                prev=curr
                curr=front

            first=head
            second=prev

            while second:
                if first.val!=second.val:
                    return False
                first=first.next
                second=second.next
            return True
