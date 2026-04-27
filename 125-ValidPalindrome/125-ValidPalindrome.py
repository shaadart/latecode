# Last updated: 4/27/2026, 8:55:19 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        new = "".join([char for char in s if char.isalnum()]).lower()
4        return new == new[::-1]
5        