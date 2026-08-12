# Last updated: 12/08/2026, 10:24:00
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3
4        if not grid: 
5            return 0
6
7        rows, cols = len(grid), len(grid[0])
8        island = 0 
9
10        def dfs(r,c):
11            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == "0":
12                return 
13
14            grid[r][c]="0"
15
16            dfs(r+1, c)
17            dfs(r-1, c)
18            dfs(r, c+1)
19            dfs(r, c-1)
20
21        for r in range(rows):
22            for c in range(cols):
23                if grid[r][c] == "1":
24                    dfs(r,c)
25                    island +=1
26
27        return island 
28        