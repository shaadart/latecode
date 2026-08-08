# Last updated: 08/08/2026, 17:36:21
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1]))
4
5
6    def helper(self, nums):
7        r1, r2 = 0,0
8        for i in nums:
9            nr = max(r1+i, r2)
10            r1 = r2
11            r2 = nr
12
13        return r2
14        
15        
16
17