# Last updated: 5/2/2026, 10:02:48 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n=len(nums)
7        countzero = 0
8        temp = []
9        for i in range(n):
10            if nums[i] == 0:
11                countzero += 1
12
13            else: 
14                temp.append(nums[i])
15
16        for j in range(countzero):
17            temp.append(0)
18
19        nums[:] = temp
20
21            
22        
23
24            
25
26