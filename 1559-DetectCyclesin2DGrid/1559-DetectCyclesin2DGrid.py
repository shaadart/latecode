# Last updated: 4/27/2026, 12:26:31 AM
1class Solution:
2    def containsCycle(self, grid: List[List[str]]) -> bool:
3        rows = len(grid)
4        cols = len(grid[0])
5        visited = [[False for _ in range(cols)] for _ in range(rows)]
6
7        def dfs(r,c,pr,pc, char):
8            directions = [(0,1), (1,0), (0,-1), (-1,0)]
9            visited[r][c] = True
10
11            for dr, dc in directions:
12                nr = r + dr
13                nc = c + dc
14
15                #chhecking bowunds
16                if nr < 0 or nr>=rows or nc<0 or nc>=cols:
17                    continue
18
19                #same char check
20                if grid[nr][nc] != char:
21                    continue
22
23                #cycle 4 length auto check
24                if nr == pr and nc == pc:
25                    continue
26
27                if visited[nr][nc]:
28                    return True
29
30                #coninue dfs
31                if dfs (nr, nc, r,c, char):
32                    return True
33
34
35            return False
36
37        for i in range(rows):
38            for j in range(cols):
39                if not visited[i][j]:
40                    if dfs(i,j, -1,-1 , grid[i][j]):
41                        return True
42
43        return False
44                
45