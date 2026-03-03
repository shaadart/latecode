# Last updated: 3/3/2026, 8:00:12 PM
1class Solution:
2    def minSwaps(self, grid):
3        n = len(grid)
4        
5        # Count trailing zeros
6        trailing = []
7        for row in grid:
8            count = 0
9            for num in reversed(row):
10                if num == 0:
11                    count += 1
12                else:
13                    break
14            trailing.append(count)
15        
16        swaps = 0
17        
18        for i in range(n):
19            required = n - 1 - i
20            j = i
21            
22            # Find suitable row
23            while j < n and trailing[j] < required:
24                j += 1
25            
26            if j == n:
27                return -1
28            
29            # Move row up step-by-step
30            while j > i:
31                trailing[j], trailing[j-1] = trailing[j-1], trailing[j]
32                swaps += 1
33                j -= 1
34        
35        return swaps