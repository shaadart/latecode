# Last updated: 21/08/2026, 00:59:59
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        
4        rows = len(matrix)
5        cols = len(matrix[0])
6
7        top = 0
8        bottom = rows - 1
9        left = 0
10        right = cols - 1
11
12        total = rows*cols
13        counter = 0 
14        out = []
15
16        while counter < total : 
17            for i in range(left, right+1):
18                out.append(matrix[top][i])
19                counter +=1
20
21            top+=1
22            if counter >= total:
23                break
24
25            for i in range(top, bottom+1):
26                out.append(matrix[i][right])
27                counter+=1
28
29            right-=1
30            if counter >= total:
31                break
32
33            for i in range(right, left-1,-1):
34                out.append(matrix[bottom][i])
35                counter+=1
36            
37            bottom-=1
38
39            if counter >= total:
40                break
41
42            for i in range(bottom, top-1, -1):
43                out.append(matrix[i][left])
44                counter+=1
45
46            left+=1
47
48
49
50        return out
51                
52
53
54
55
56        