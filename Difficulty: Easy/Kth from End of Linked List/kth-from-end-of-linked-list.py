""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        # code here
        slow = head 
        fast = head 
        
        for i in range(k):
            if fast is None:
                return -1 
                
            fast = fast.next
            
        while fast : 
            slow = slow.next
            fast = fast.next
            
        return slow.data
        