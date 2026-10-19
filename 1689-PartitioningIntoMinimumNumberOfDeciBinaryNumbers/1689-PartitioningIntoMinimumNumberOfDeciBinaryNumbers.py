# Last updated: 19/10/2026, 16:23:09
class Solution:
    def minPartitions(self, n: str) -> int:
        return ord(max(x for x in n))-ord('0')