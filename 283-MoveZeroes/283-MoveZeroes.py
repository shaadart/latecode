# Last updated: 20/08/2026, 12:07:43
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n=len(nums)
7        countzero = 0
8        temp = []
9
10        for i in nums:
11            if i == 0:
12                continue
13            else:
14                temp.append(i)
15
16        trun = len(nums)-len(temp)
17
18        for i in range(trun):
19            temp.append(0)
20
21        nums[:] = temp