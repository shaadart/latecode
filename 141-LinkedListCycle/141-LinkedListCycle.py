# Last updated: 14/11/2026, 13:18:02
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        curr = head
10        slow = curr
11        fast = curr
12
13        while fast and fast.next:
14            slow = slow.next
15            fast = fast.next.next
16            if fast == slow:
17                return True
18
19        return False
20        