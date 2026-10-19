# Last updated: 19/10/2026, 16:26:15
import math 
class Solution(object):
    def search(self, nums, target):
        
        left, right = 0, len(nums)-1

        while(left<=right):
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            elif nums[mid]< target:
                left = mid +1

            else:
                right = mid -1

        return -1



