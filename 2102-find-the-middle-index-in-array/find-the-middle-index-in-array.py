class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        leftsum = 0
        rightsum = sum(nums)
        n = len(nums)
        i = 0
        while i<n:
            rightsum -= nums[i]
            if leftsum == rightsum:
                return i

            leftsum += nums[i]


            i+=1
        return -1
