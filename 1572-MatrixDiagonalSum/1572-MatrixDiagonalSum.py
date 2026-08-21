# Last updated: 21/08/2026, 07:15:03
1class Solution:
2    def diagonalSum(self, mat: List[List[int]]) -> int:
3        n = len(mat)
4        out = []
5
6        if n % 2 == 0:
7            for i in range(n):
8
9                for j in range(n):
10
11                    if i == j:
12                        out.append(mat[i][j])
13
14            r, c = 0, n - 1
15            while c >= 0 and r < n:
16                out.append(mat[r][c])
17
18                r += 1
19                c -= 1
20
21        else:
22            for i in range(n):
23
24                for j in range(n):
25
26                    if i == j:
27                        out.append(mat[i][j])
28
29            r, c = 0, n - 1
30
31            while c >= 0 and r < n:
32                if r == c:
33                    r += 1
34                    c -= 1
35                    continue  
36
37                out.append(mat[r][c])
38                
39                r += 1
40                c -= 1
41
42
43            
44
45        return sum(out)
46