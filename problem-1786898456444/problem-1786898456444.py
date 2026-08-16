# Last updated: 16/08/2026, 22:10:56
1class Solution:
2    def reverse(self, x: int) -> int:
3
4        o = x
5        isneg = False
6        rev = 0
7
8        if x < 0:
9            isneg = True
10            x = abs(x)
11
12        while x > 0:
13            dig = x % 10
14            rev = rev * 10 + dig
15            x //= 10
16
17        if rev < -2**31 or rev > 2**31 - 1:
18            return 0
19
20        return rev if isneg == False else (-rev)