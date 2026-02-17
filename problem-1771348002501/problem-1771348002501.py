# Last updated: 2/17/2026, 10:36:42 PM
1# class Solution:
2#     def maxFrequencyElements(self, nums: List[int]) -> int:
3#         maxCount = 1
4
5#         for i in range(len(nums)):
6#             curCount = nums.count(nums[i])
7#             if (curCount > maxCount):
8#                 maxCount = curCount
9#             elif (curCount == maxCount and maxCount > 1):
10#                 maxCount += curCount
11
12#             else:
13#                 continue
14
15#         if maxCount == 1: 
16#             print("this is triggered")
17#             return len(nums)
18
19#         else: 
20#             return maxCount
21
22class Solution:
23    def maxFrequencyElements(self, nums: List[int]) -> int:
24        maxFreq = 0
25        total = 0
26        seen = []   # track processed numbers
27
28        for i in range(len(nums)):
29            if nums[i] in seen:
30                continue
31
32            curFreq = nums.count(nums[i])
33            seen.append(nums[i])
34
35            if curFreq > maxFreq:
36                maxFreq = curFreq
37                total = curFreq
38            elif curFreq == maxFreq:
39                total += curFreq
40
41        return total
42