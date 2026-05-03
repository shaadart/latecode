class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod = nums[0]
        maxprod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0: 
                maxprod, minprod = minprod, maxprod

            maxprod = max(nums[i] , maxprod * nums[i])
            minprod = min(nums[i] , minprod * nums[i])



            result = max(maxprod, result)
        return result

        