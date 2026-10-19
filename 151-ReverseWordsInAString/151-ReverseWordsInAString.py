# Last updated: 19/10/2026, 16:30:04
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
