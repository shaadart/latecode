# Last updated: 21/09/2026, 12:10:19
1class Solution:
2    def trailingZeroes(self, n: int) -> int:
3        res = 1
4
5        for i in range(1, n+1):
6            res*=i
7
8        cz = 0 
9
10        while res > 0 and res%10==0:
11            cz+=1
12            res//=10
13
14        return cz
15
16
17        