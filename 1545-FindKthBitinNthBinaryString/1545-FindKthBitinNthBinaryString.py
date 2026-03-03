# Last updated: 3/4/2026, 5:29:35 AM
1class Solution:
2    def findKthBit(self, n: int, k: int) -> str:
3        
4        if n == 1:
5            return "0"
6        
7        mid = 1 << (n - 1)  # 2^(n-1)
8        
9        if k == mid:
10            return "1"
11        
12        if k > mid:
13            mirrored = 2 * mid - k
14            bit = self.findKthBit(n - 1, mirrored)
15            return "1" if bit == "0" else "0"
16        
17        return self.findKthBit(n - 1, k)