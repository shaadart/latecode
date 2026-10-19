# Last updated: 19/10/2026, 16:20:37
class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for x in nums:
            # 2 is the only impossible prime
            if x == 2:
                ans.append(-1)
                continue

            # Find the rightmost 0 bit
            # (~x) & (x + 1) isolates it
            rightmost_zero = (~x) & (x + 1)

            # Flip that bit and zero out everything to the right
            ans.append(x - (rightmost_zero >> 1))

        return ans
