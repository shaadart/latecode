# Last updated: 19/10/2026, 16:19:24
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        i = 0
        maxlen = 0

        for j in range(n):
            while i <= j and nums[j] > k * nums[i]:
                i += 1
            maxlen = max(maxlen, j - i + 1)

        return n - maxlen
