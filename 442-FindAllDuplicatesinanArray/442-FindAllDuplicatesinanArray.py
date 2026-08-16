# Last updated: 16/08/2026, 18:37:28
1class Solution:
2    def findDuplicates(self, nums: List[int]) -> List[int]:
3        seen = set()
4        out = []
5
6        for i in range(len(nums)):
7            if nums[i] in seen:
8                out.append(nums[i])
9
10            else:
11                seen.add(nums[i])
12
13        return out