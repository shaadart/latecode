# Last updated: 5/4/2026, 8:15:42 PM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        n = len(matrix)
4
5        for i in range(n):
6            #transpose-ing
7            for j in range(i,n):
8                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
9
10        #reverse
11        for row in matrix:
12            row.reverse()
13
14        
15        