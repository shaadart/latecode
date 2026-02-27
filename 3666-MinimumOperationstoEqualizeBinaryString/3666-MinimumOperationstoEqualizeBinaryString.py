# Last updated: 2/28/2026, 12:07:30 AM
1class Solution: #dint did on my own :(
2    def minOperations(self, s: str, k: int) -> int:
3        n = len(s)
4        z = s.count('0')
5        
6        if z == 0:
7            return 0
8        if n == k:
9            return 1 if z == n else -1
10
11        b = n - k
12        k1 = (z + k - 1) // k
13        res = float('inf')
14        
15        # Case 1: x is Odd
16        if (k & 1) == (z & 1):
17            t = (n - z + b - 1) // b
18            res = max(k1, t) | 1
19
20        # Case 2: x is Even
21        if (z & 1) == 0:
22            t = (z + b - 1) // b
23            e = max(k1, t)
24            e += e & 1
25            if e < res:
26                res = e
27
28        return -1 if res == float('inf') else res
29
30