# Last updated: 16/08/2026, 13:04:27
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3
4        seen = set()
5
6        for num in nums:
7            seen.add(num)
8
9        k = sorted(seen)
10
11        if len(k) == len(nums):
12            return False
13
14        return True
15        