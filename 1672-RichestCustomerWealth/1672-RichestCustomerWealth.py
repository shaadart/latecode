# Last updated: 21/08/2026, 09:22:31
1class Solution:
2    def maximumWealth(self, accounts: List[List[int]]) -> int:
3        rich = 0
4        for i in accounts:
5            rich = max(sum(i), rich)
6
7        return rich
8        