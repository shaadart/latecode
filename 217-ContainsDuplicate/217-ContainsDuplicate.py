# Last updated: 4/27/2026, 11:12:15 AM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        hashset = set()
4        for n in nums:
5            if n in hashset:
6                return True
7
8            hashset.add(n)
9
10        return False