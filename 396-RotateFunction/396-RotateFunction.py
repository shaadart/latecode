# Last updated: 5/2/2026, 10:03:49 PM
1class Solution:
2    def maxRotateFunction(self, A: List[int]) -> int:
3        a_sum = 0
4        F = 0
5        n = len(A)
6
7        for i in range(n):
8            a_sum += A[i]
9            F += i * A[i]
10
11        res = F
12
13        for i in range(1, n):
14            F += a_sum - n * A[-i]
15            res = max(res, F)
16
17        return res