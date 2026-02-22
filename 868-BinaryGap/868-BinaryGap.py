# Last updated: 2/23/2026, 12:03:19 AM
1class Solution:
2    def binaryGap(self, n: int) -> int:
3        binary = bin(n)[2:]   
4        
5        max_dist = 0
6        last_index = -1
7        
8        for i in range(len(binary)):
9            if binary[i] == '1':
10                if last_index != -1:
11                    max_dist =  max(i-last_index, max_dist)
12
13                last_index = i
14
15        return max_dist
16                    
17                