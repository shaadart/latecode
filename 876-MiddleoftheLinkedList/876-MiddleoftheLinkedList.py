# Last updated: 5/6/2026, 11:12:53 PM
1# Definition for singly-linked list.
2class ListNode:
3    def __init__(self, val=0, next=None):
4        self.val = val
5        self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        #count
10        count = 0
11        curr = head
12        while curr!= None:
13            curr = curr.next
14            count += 1
15
16        curr = head
17        for i in range(count//2):
18
19            curr = curr.next
20
21        return curr
22            
23
24
25        