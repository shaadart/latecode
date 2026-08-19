# Last updated: 20/08/2026, 02:07:01
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        spl = s.split()
4        return len(spl[-1])
5        