# Last updated: 2/15/2026, 1:58:54 AM
1class Solution:
2
3    
4
5    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
6        t = [[0,0] * 101 for _ in range(101)] # this shit will create 101 x 101 matrix
7        t[0][0] = float(poured)
8
9        for row in range(query_row + 1):
10            for col in range (row+1):
11                extra = (t[row][col] -1 ) / 2.0
12                if extra > 0: 
13                    t[row+1][col] += extra 
14                    t[row+1][col+1] += extra 
15
16
17
18        return min(1.0,t[query_row][query_glass])
19
20
21        