# Last updated: 5/7/2026, 10:30:15 AM
1# Definition for singly-linked list.
2class ListNode:
3    def __init__(self, val=0, next=None):
4        self.val = val
5        self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        slow = head
10        fast = head
11
12        while fast!= None and fast.next != None:
13                slow = slow.next
14                fast = fast.next.next
15
16        return slow
17
18
19        