class Solution:
    def insertAtHead(self, ListNode,head, x):

        newNode = ListNode(x)
        newNode.next = head

        return newNode