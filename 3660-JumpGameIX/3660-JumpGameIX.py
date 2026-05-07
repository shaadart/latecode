# Last updated: 5/8/2026, 12:09:46 AM
1class Solution:
2    def maxValue(self, a: List[int]) -> List[int]:
3        b = zip([*accumulate(a,max)][::-1],accumulate([inf]+a[::-1],min))
4        return [*accumulate(b,lambda q,p:p[0]>p[1] and q or p[0],initial=0)][:0:-1]