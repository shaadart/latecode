# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getlen(h):
            curr = h
            count = 0
            while curr:
                count+=1
                curr=curr.next

            return count

        lenA = getlen(headA)
        lenB = getlen(headB)

        
        #match
        currB,currA = headB,headA
        while max(lenA, lenB)!= min(lenA,lenB):
            if lenB > lenA:
                currB = currB.next
                lenB-=1

            else:
                currA = currA.next
                lenA-=1

        
        #check
        while currA:
            if currA == currB:
                return currA

            currA= currA.next
            currB= currB.next

            
                

        