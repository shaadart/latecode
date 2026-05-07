# Last updated: 5/7/2026, 2:29:19 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
9        def getlen(h):
10            curr = h
11            count = 0
12            while curr:
13                count+=1
14                curr=curr.next
15
16            return count
17
18        lenA = getlen(headA)
19        lenB = getlen(headB)
20
21        
22        #match
23        currB,currA = headB,headA
24        while max(lenA, lenB)!= min(lenA,lenB):
25            if lenB > lenA:
26                currB = currB.next
27                lenB-=1
28
29            else:
30                currA = currA.next
31                lenA-=1
32
33        
34        #check
35        while currA:
36            if currA == currB:
37                return currA
38
39            currA= currA.next
40            currB= currB.next
41
42            
43                
44
45        