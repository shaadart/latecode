# Last updated: 3/3/2026, 8:01:42 PM
1class Solution:
2    def minPartitions(self, n: str) -> int:
3        return ord(max(x for x in n))-ord('0')