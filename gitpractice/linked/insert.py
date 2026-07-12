class Solution:
    def insertAtHead(self, ListHead, x):

        newNode = ListNode(x)
        newNode.next = ListHead

        return newNode