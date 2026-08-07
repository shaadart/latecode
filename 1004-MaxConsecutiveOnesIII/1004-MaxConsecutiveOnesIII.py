# Last updated: 07/08/2026, 10:30:04
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        zeros, longest, left = 0,0,0
4        n = len(nums)
5
6        for right in range(n):
7            if nums[right] == 0:
8                zeros+=1
9
10            while zeros > k :
11                if nums[left] == 0:
12                    zeros-=1
13
14                left+=1
15
16            longest = max(longest, (right-left +1))
17
18        return longest
19        