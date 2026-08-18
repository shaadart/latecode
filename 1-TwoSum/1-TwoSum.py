# Last updated: 18/08/2026, 14:04:25
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        # Changed from a set() to a dictionary to store {value: index}
4        seen = {} 
5        n = len(nums)
6        
7        for i in range(n):
8            complement = target - nums[i]
9
10            if complement in seen:
11                return [seen[complement], i]
12
13            seen[nums[i]] = i          