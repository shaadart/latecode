class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r,c,pr,pc, char):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            visited[r][c] = True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                #chhecking bowunds
                if nr < 0 or nr>=rows or nc<0 or nc>=cols:
                    continue

                #same char check
                if grid[nr][nc] != char:
                    continue

                #cycle 4 length auto check
                if nr == pr and nc == pc:
                    continue

                if visited[nr][nc]:
                    return True

                #coninue dfs
                if dfs (nr, nc, r,c, char):
                    return True


            return False

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if dfs(i,j, -1,-1 , grid[i][j]):
                        return True

        return False
                
