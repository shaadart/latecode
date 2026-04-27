# Last updated: 4/28/2026, 1:00:18 AM
1from typing import List
2from collections import deque
3
4class Solution:
5    def hasValidPath(self, grid: List[List[int]]) -> bool:
6        m, n = len(grid), len(grid[0])
7
8        dirs = [
9            (0, -1),
10            (0, 1),
11            (-1, 0),
12            (1, 0)
13        ]
14
15        street_dirs = {
16            1: [0, 1],
17            2: [2, 3],
18            3: [0, 3],
19            4: [1, 3],
20            5: [0, 2],
21            6: [1, 2],
22        }
23
24        opposite = {0: 1, 1: 0, 2: 3, 3: 2}
25
26        visited = [[False] * n for _ in range(m)]
27        q = deque([(0, 0)])
28        visited[0][0] = True
29
30        while q:
31            r, c = q.popleft()
32
33            if r == m - 1 and c == n - 1:
34                return True
35
36            for d in street_dirs[grid[r][c]]:
37                nr = r + dirs[d][0]
38                nc = c + dirs[d][1]
39
40                if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
41                    continue
42
43                next_type = grid[nr][nc]
44
45                if opposite[d] in street_dirs[next_type]:
46                    visited[nr][nc] = True
47                    q.append((nr, nc))
48
49        return False