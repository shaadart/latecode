# Last updated: 6/17/2026, 11:35:45 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        currIdx = 0
4        finalJump = len(nums) - 1
5
6        for i in range(len(nums)):
7            if i > currIdx:
8                return False
9            
10
11            jump = nums[i]
12            currIdx = max(currIdx, i + jump)
13
14            if currIdx >= finalJump:
15                
16                return True
17
18        return True