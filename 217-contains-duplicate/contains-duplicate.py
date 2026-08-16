class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            seen.add(num)

        k = sorted(seen)

        if len(k) == len(nums):
            return False

        return True
        