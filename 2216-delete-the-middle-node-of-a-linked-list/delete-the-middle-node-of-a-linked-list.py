# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        
        # If only one node exists
        if head is None or head.next is None:
            return None

        # Count nodes
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        # Find node before middle
        middle = count // 2

        curr = head
        for i in range(middle - 1):
            curr = curr.next

        # Delete middle node
        curr.next = curr.next.next

        return head