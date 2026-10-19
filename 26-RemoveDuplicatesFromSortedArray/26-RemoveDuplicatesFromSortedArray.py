# Last updated: 19/10/2026, 16:33:07
class Solution(object):
    def removeDuplicates(self, nums):
        # 3,4,4,5,5,5,5,7,7,9
        # 3,4,5,7,9

        start = 0

        for i in range(1,len(nums)):
            if nums[i]!=nums[start]:
                start += 1
                nums[start] = nums[i]

            
        return start+1



