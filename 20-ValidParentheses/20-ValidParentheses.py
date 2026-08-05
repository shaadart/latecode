# Last updated: 05/08/2026, 12:08:57
1class Solution:
2    def isValid(self, s: str) -> bool:
3        #defination
4        stack = []
5        bracketmap = {")": "(", "}": "{", "]": "["}
6
7        for ch in s:
8            if ch in "([{":
9                stack.append(ch)
10
11            else:
12                if not stack:
13                    return False
14
15                if stack.pop() != bracketmap[ch]:
16                    return False
17
18
19        return len(stack) == 0