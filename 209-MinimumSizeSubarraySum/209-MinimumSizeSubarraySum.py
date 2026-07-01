# Last updated: 7/1/2026, 1:48:30 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        mini=float("inf")
        s=0
        n=len(nums)
        for right in range(n):
            s +=nums[right]
            while s>=target:
                mini=min(mini,right-left+1)
                s-=nums[left]
                left +=1
        return mini if mini!=float("inf") else 0