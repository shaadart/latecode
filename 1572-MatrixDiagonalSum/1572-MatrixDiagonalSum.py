# Last updated: 21/08/2026, 07:32:50
1class Solution:
2    def diagonalSum(self, mat: List[List[int]]) -> int:
3        n = len(mat)
4        total=0
5
6        for i in range(n):
7            total += mat[i][i]
8
9            total += mat[i][n-1-i]
10
11        if n%2!=0:
12            mid = n // 2
13            total-= mat[mid][mid]
14
15
16        return total
17