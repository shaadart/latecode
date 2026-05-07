# Last updated: 5/7/2026, 12:45:18 PM
1class Solution:
2    def isPalindrome(self, head: Optional[ListNode]) -> bool:
3
4        arr = []
5
6        curr = head
7
8        while curr: 
9            arr.append(curr.val)
10            curr = curr.next
11
12        return arr == arr[::-1]