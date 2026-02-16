# Last updated: 2/16/2026, 7:16:53 AM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        if n==0:
4            return 0
5
6        result = 0
7
8        for i in range(32):
9            result <<= 1
10
11            result = (result | n & 1)
12
13            n >>=1
14
15        
16        return result
17
18
19        
20
21
22