class Solution:
    def searchKey(self, head, key):

        while head:

            if head.val == key:
                return True

            head = head.next

        return False