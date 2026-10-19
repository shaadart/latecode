# Last updated: 19/10/2026, 16:26:45
class Solution(object):
    def findErrorNums(self, nums):
        seen = set()
        duplicate = -1
        n = len(nums)

        for x in nums:
            if x in seen:
                duplicate = x
            seen.add(x)

        # missing number = 1..n sum minus seen sum
        total = n * (n + 1) // 2
        missing = total - sum(seen)

        return [duplicate, missing]
