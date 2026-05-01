# Last updated: 5/1/2026, 9:22:06 AM
1class Solution:
2    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
3        n=len(words)
4        n2=n//2+1
5        for d in range(n2):
6            l=startIndex-d if startIndex>=d else n+startIndex-d
7            r=startIndex+d-n if startIndex+d>=n else startIndex+d
8            if words[l]==target or words[r]==target: return d
9        return -1