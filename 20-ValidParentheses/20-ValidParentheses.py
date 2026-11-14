# Last updated: 14/11/2026, 12:27:57
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        brackets = {"}":"{", ")":"(", "]":"[" }
5
6        for i in s:
7            if i in list(brackets.values()):
8                stack.append(i)
9
10            elif i in list(brackets.keys()):
11                if not stack:
12                    return False
13                
14                if brackets[i]!=stack[-1]:
15                    return False
16                
17                stack.pop(-1)
18                
19
20        
21        return len(stack)==0