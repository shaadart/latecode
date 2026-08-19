# Last updated: 20/08/2026, 02:16:35
1class Solution:
2    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
3        arr.sort()
4
5        diff = arr[1] - arr[0]
6        i = 1
7        n = len(arr)
8        while i < n:
9            if arr[i] - arr[i-1] == diff:
10                i+=1
11                continue
12
13            else:
14                return False
15
16        return True
17
18
19        