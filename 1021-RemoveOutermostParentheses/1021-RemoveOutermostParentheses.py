# Last updated: 08/10/2026, 13:43:05
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        res, lvl = [], 0
4        for b in s:
5            if b == ")":
6                lvl -= 1 
7
8            if lvl>0:
9                res.append(b)
10            if b == "(":
11                lvl +=1
12
13        return "".join(res) 
14
15        