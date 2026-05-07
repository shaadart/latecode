# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head

        if head == None or head.next == None:
            return head
     

        while fast!=None and fast.next!=None: 
            if fast.next.val == fast.val:
                fast.next = fast.next.next
            else:
                fast = fast.next

        return head


        