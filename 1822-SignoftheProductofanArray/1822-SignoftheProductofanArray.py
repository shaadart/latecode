# Last updated: 20/08/2026, 02:11:55
1class Solution:
2    def arraySign(self, nums: List[int]) -> int:
3        p = 1
4        for i in nums:
5            p = p * i
6
7        print(p)
8        if p == 0:
9            return 0
10
11        elif p >= 0:
12            return 1
13
14        elif p<=0:
15            return -1
16