# Last updated: 3/6/2026, 2:44:53 AM
1class Solution:
2    def minOperations(self, s: str) -> int:
3
4        n = len(s)
5
6        startw0 = 0  # 01010101..
7        startw1 = 0  # 10101010..
8
9        for i in range(n):
10            if i % 2 == 0:
11                if s[i] != '0':
12                    startw0 += 1
13                if s[i] != '1':
14                    startw1 += 1
15            else:
16                if s[i] != '1':
17                    startw0 += 1
18                if s[i] != '0':
19                    startw1 += 1
20
21        return min(startw0, startw1)