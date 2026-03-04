# Last updated: 3/4/2026, 1:54:09 PM
1class Solution:
2    def numSpecial(self, mat: List[List[int]]) -> int:
3        def check_row(row):
4            if row.count(1) == 1:
5                return True 
6            return False
7
8        def check_column(c, j):
9            count = 0
10            for row in range(len(c)):
11                if mat[row][j] == 1:
12                    count +=1
13               
14            if count==1:
15                return True 
16            else:
17                return False
18
19        c = 0
20        for i in range(len(mat)):
21            for j in range(len(mat[0])):
22
23                if mat[i][j] == 1: 
24                    if check_row(mat[i]) and check_column(mat, j):
25                        c+=1   
26
27        return c             
28
29            
30
31
32        