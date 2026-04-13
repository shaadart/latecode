# Last updated: 4/14/2026, 12:21:54 AM
1class Solution:
2    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
3        answer = float('inf')
4
5        for i in range(len(nums)):
6            if nums[i] == target:
7                answer = min(answer, abs(i - start))
8
9        return answer