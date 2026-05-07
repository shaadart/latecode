# Last updated: 5/7/2026, 11:05:45 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        fast = head
10
11        if head == None or head.next == None:
12            return head
13     
14
15        while fast!=None and fast.next!=None: 
16            if fast.next.val == fast.val:
17                fast.next = fast.next.next
18            else:
19                fast = fast.next
20
21        return head
22
23
24        