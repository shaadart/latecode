# Last updated: 11/08/2026, 17:19:13
1class Solution:
2    def missingInteger(self, nums: List[int]) -> int:
3
4        i = 1
5        stk = [nums[0]]
6        while i < len(nums) and nums[i] == stk[-1]+1:
7            stk.append(nums[i])
8            i+=1
9            
10
11        tot = sum(stk)
12
13        print(tot)
14
15        while tot in nums:
16            tot+=1
17
18        return tot
19
20
21
22
23        