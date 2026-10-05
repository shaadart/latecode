# Last updated: 05/10/2026, 18:34:58
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
8        if head is None or head.next is None:
9            return None
10
11
12        fast, slow = head, head
13        prev = None
14        count = 0
15        while fast is not None and fast.next is not None:
16            prev = slow
17            slow = slow.next
18            fast = fast.next.next
19            
20       
21        prev.next=slow.next
22
23        return head
24
25
26
27        
28            
29
30        
31
32        