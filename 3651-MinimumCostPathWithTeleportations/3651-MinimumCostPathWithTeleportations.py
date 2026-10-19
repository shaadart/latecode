# Last updated: 19/10/2026, 16:20:03
class Solution:
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        INF = 10**18

        # Collect and sort cells by grid value
        cells = [(i, j) for i in range(m) for j in range(n)]
        cells.sort(key=lambda x: grid[x[0]][x[1]])

        # cost[i][j] = min cost to reach destination from (i, j)
        cost = [[INF] * n for _ in range(m)]

        for _ in range(k + 1):

            # ---- TELEPORT RELAXATION ----
            min_cost_so_far = INF
            start = 0

            for idx, (x, y) in enumerate(cells):
                min_cost_so_far = min(min_cost_so_far, cost[x][y])

                # group same-value cells together
                if idx + 1 < len(cells) and grid[x][y] == grid[cells[idx + 1][0]][cells[idx + 1][1]]:
                    continue

                # update all cells with same value
                for j in range(start, idx + 1):
                    cx, cy = cells[j]
                    cost[cx][cy] = min(cost[cx][cy], min_cost_so_far)

                start = idx + 1

            # ---- NORMAL DP (RIGHT + DOWN) ----
            for i in reversed(range(m)):
                for j in reversed(range(n)):
                    if i == m - 1 and j == n - 1:
                        cost[i][j] = 0
                        continue

                    if i + 1 < m:
                        cost[i][j] = min(cost[i][j], grid[i + 1][j] + cost[i + 1][j])

                    if j + 1 < n:
                        cost[i][j] = min(cost[i][j], grid[i][j + 1] + cost[i][j + 1])

        return cost[0][0]
