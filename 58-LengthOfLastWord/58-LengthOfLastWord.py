# Last updated: 19/10/2026, 16:32:18
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spl = s.split()
        return len(spl[-1])
        