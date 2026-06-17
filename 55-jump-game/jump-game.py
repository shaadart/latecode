class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currIdx = 0
        finalJump = len(nums) - 1

        for i in range(len(nums)):
            if i > currIdx:
                return False
            

            jump = nums[i]
            currIdx = max(currIdx, i + jump)

            if currIdx >= finalJump:
                
                return True

        return True