# Last updated: 2/26/2026, 4:59:42 PM
1class Solution:
2    def numSteps(self, s: str) -> int:
3        def isOdd(n):
4            return n % 2 != 0
5
6        rep = int(s, 2)
7        counter = 0
8        while rep != 1:
9            if isOdd(rep):
10                rep= rep+1
11                counter+=1
12            else: 
13                rep = rep//2
14                counter+=1
15
16        return counter
17