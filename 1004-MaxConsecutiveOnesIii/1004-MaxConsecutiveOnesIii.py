# Last updated: 19/10/2026, 16:25:24
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros, left, res = 0,0,0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros+=1
            
            while zeros > k:
                if nums[left] == 0:
                    zeros-=1
                left+=1

            res = max(res, right-left+1)


        return res

        

        