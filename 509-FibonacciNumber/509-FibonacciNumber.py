# Last updated: 09/08/2026, 23:04:29
1class Solution:
2    def fib(self, n: int) -> int:
3        if n ==1:
4            return 1
5
6        elif n == 0:
7            return 0
8
9        
10        else: 
11            return self.fib(n-2) + self.fib(n-1)
12
13        
14        