# Last updated: 5/7/2026, 12:39:15 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8       
9        curr = head
10        prev = None
11        nxt = None
12
13        while curr!= None:
14            nxt = curr.next
15            curr.next = prev
16            prev = curr
17            curr = nxt
18
19
20        return prev
21        