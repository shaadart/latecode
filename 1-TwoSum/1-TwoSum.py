# Last updated: 4/30/2026, 9:18:40 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hash = {}
4
5        for i, num in enumerate(nums):
6            complement = target - num
7            if complement in hash:
8                return [hash[complement], i]
9            hash[num] = i