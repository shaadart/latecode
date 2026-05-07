class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        arr = []

        curr = head

        while curr: 
            arr.append(curr.val)
            curr = curr.next

        return arr == arr[::-1]