class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros, longest, left = 0,0,0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                zeros+=1

            while zeros > k :
                if nums[left] == 0:
                    zeros-=1

                left+=1

            longest = max(longest, (right-left +1))

        return longest
        