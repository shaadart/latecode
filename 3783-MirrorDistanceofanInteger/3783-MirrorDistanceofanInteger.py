# Last updated: 4/19/2026, 3:15:03 AM
1class Solution:
2    def mirrorDistance(self, n: int) -> int:
3        def reverse(n):
4            reverse = 0 
5            while n != 0:
6                digit = n % 10
7                reverse = (reverse*10) + digit 
8                n = n // 10
9
10            return reverse
11
12        return abs(reverse(n) - n)
13
14
15        