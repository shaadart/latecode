# Last updated: 6/13/2026, 12:52:10 PM
1# import collections
2
3class Solution:
4    def simplifyPath(self, path: str) -> str:
5
6        stack = []
7        components = path.split('/')
8        
9        for component in components:
10            if component == "." or component == "":
11                continue
12            
13            elif component == '..':
14                if stack:
15                    stack.pop()
16
17            else:
18                stack.append(component)
19
20            
21        return "/" + "/".join(stack)
22
23
24        