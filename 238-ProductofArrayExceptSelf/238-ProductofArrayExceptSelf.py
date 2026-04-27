# Last updated: 4/27/2026, 1:10:14 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        output = [1] * n
5        prefix = 1
6        #prefix table
7        for i in range(n):
8            output[i] = prefix
9            prefix = prefix * nums[i] 
10
11
12
13        postfix = 1
14
15        for i in range(n-1, -1, -1):
16            output[i] = output[i] * postfix
17            postfix = postfix * nums[i]
18
19        return output
20
21
22
23        