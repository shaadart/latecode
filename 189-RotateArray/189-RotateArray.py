# Last updated: 6/13/2026, 11:45:28 AM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        
4
5        n = len(nums)
6        k %= n 
7        r = nums[:n-k]
8        l = nums[n-k:]
9        nums[:] = l+r
10            
11        