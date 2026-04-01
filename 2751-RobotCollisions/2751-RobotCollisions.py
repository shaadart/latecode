# Last updated: 4/1/2026, 11:46:30 PM
1from typing import List
2
3class Solution:
4    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
5
6        n = len(positions)
7        indices = sorted(range(n), key=lambda i: positions[i])
8
9        stack = []
10
11        for i in indices:
12            if directions[i] == 'R':
13                stack.append(i)
14            else:
15                while stack and healths[i] > 0:
16                    j = stack.pop()
17
18                    if healths[j] > healths[i]:
19                        healths[j] -= 1
20                        healths[i] = 0
21                        stack.append(j)
22
23                    elif healths[j] < healths[i]:
24                        healths[i] -= 1
25                        healths[j] = 0
26
27                    else:  # equal health
28                        healths[i] = 0
29                        healths[j] = 0
30
31        # collect survivors
32        result = []
33        for i in range(n):
34            if healths[i] > 0:
35                result.append(healths[i])
36
37        return result