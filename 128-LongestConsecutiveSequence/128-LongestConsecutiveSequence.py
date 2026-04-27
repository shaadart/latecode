# Last updated: 4/27/2026, 8:34:21 PM
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
13        for i in range(1, n):
14            if nums[i] == nums[i-1]:
15                continue  # skip duplicates
16
17            if nums[i] == nums[i-1] + 1:
18                temp.append(nums[i])
19            else:
20                if len(temp) > len(out):
21                    out = temp[:]
22                temp = [nums[i]]
23
24        # final check
25        if len(temp) > len(out):
26            out = temp
27
28        return len(out)