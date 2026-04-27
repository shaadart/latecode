class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join([char for char in s if char.isalnum()]).lower()
        return new == new[::-1]
        