# Last updated: 14/11/2026, 14:40:25
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
8        res = ListNode()
9        head = res
10
11        while list1 and list2: 
12            if list1.val <= list2.val:
13                head.next = list1
14                list1 = list1.next
15
16            else:
17                head.next = list2
18                list2 = list2.next
19
20            head = head.next
21            
22        if list1:
23            head.next = list1
24
25        if list2:
26            head.next = list2
27
28        return res.next
29
30
31            
32
33        
34
35        