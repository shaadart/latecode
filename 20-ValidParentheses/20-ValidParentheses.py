# Last updated: 6/14/2026, 10:07:24 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        #defination
4        stack = []
5        rev_bracket_map = {")": "(", "}": "{", "]": "["}
6
7
8        spl = list(s)
9
10
11        for i in spl:
12            #opening: push
13
14            if i in ["(", "[", "{"]:
15                stack.append(i)
16
17            #closing:
18
19            elif i in [")", "]", "}"]:
20                if not stack:
21                    return False
22
23                else: 
24                    if stack[-1] == rev_bracket_map[i]:
25                        stack.pop()
26                    else:
27                        return False
28
29        return len(stack) == 0
30
31
32
33
34
35        
36        
37