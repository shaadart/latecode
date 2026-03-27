# Last updated: 3/27/2026, 3:06:59 PM
1class Solution:
2    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
3        def left_rotate(arr, d):
4            n = len(arr)
5            d = d % n 
6            return (arr == (arr[d:] + arr[:d]))
7
8        def right_rotate(arr, d):
9            n = len(arr)
10            d = d % n 
11            return (arr == (arr[-d:] + arr[:-d]))
12
13        
14        for i in range(len(mat)):
15            if i%2 != 0: 
16                if not right_rotate(mat[i],k):
17                    return False
18
19            else: 
20                if not left_rotate(mat[i],k):
21                    return False
22
23        return True
24
25
26     
27
28
29
30        
31
32
33