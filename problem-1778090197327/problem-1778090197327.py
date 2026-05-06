# Last updated: 5/6/2026, 11:26:37 PM
1# Definition for singly-linked list.
2class ListNode:
3    def __init__(self, val=0, next=None):
4        self.val = val
5        self.next = next
6
7class Solution:
8    def deleteMiddle(self, head):
9        
10        # If only one node exists
11        if head is None or head.next is None:
12            return None
13
14        # Count nodes
15        count = 0
16        curr = head
17
18        while curr:
19            count += 1
20            curr = curr.next
21
22        # Find node before middle
23        middle = count // 2
24
25        curr = head
26        for i in range(middle - 1):
27            curr = curr.next
28
29        # Delete middle node
30        curr.next = curr.next.next
31
32        return head