# Last updated: 30/08/2026, 15:45:01
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        zeros, left, res = 0,0,0
4
5        for right in range(len(nums)):
6            if nums[right] == 0:
7                zeros+=1
8            
9            while zeros > k:
10                if nums[left] == 0:
11                    zeros-=1
12                left+=1
13
14            res = max(res, right-left+1)
15
16
17        return res
18
19        
20
21        