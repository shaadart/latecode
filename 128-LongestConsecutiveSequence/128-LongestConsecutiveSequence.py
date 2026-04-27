# Last updated: 4/27/2026, 8:48:29 PM
1
2
3class Solution:
4    def longestConsecutive(self, nums: List[int]) -> int:
5        if not nums:
6            return 0
7
8        out = []
9        nums.sort()
10        n = len(nums)
11        temp = [nums[0]]
12
13        
14        for i in range(1,n):
15            if nums[i] == nums[i-1]:
16                continue
17            if nums[i] == nums[i-1] + 1:
18                temp.append(nums[i])
19
20            else:
21                if len(temp) > len(out):
22                    out = temp[:]
23
24                temp = [nums[i]]
25        if len(temp) > len(out):
26            out = temp
27
28        return len(out)