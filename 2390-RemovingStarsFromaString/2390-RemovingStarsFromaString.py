# Last updated: 24/09/2026, 18:58:59
1class Solution:
2
3    def removeStars(self, s: str) -> str:
4        stack = []
5
6
7        for char in s: 
8            if char == "*":
9                if stack:
10                    stack.pop()
11
12            else: 
13                stack.append(char)
14
15        return "".join(stack)
16
17