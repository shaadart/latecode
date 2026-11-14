# Last updated: 14/11/2026, 13:13:50
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head or not head.next:
9            return head
10
11        prev = None
12        curr= head
13
14        while curr:
15            next_node = curr.next
16            curr.next = prev
17            prev = curr
18            curr = next_node
19
20        return prev
21
22
23
24
25    
26
27
28       
29        