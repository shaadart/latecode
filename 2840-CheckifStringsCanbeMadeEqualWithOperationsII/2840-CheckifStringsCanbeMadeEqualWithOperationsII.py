# Last updated: 3/30/2026, 11:59:36 AM
1class Solution:
2    def checkStrings(self, s1: str, s2: str) -> bool:
3
4        evenMatch = sorted(s1[::2]) == sorted(s2[::2])
5        oddMatch = sorted(s1[1::2]) == sorted(s2[1::2])
6        return evenMatch and oddMatch
7        