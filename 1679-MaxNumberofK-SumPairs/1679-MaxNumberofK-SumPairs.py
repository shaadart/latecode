# Last updated: 23/08/2026, 16:10:50
1class Solution:
2    def maxOperations(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        left = 0 
5        right = len(nums)-1
6        operation = 0
7
8        while left < right:
9            if nums[left] + nums[right] == k:
10                operation +=1 
11                left +=1
12                right -=1
13
14            elif nums[left] + nums[right] < k:
15                left+=1
16
17            else:
18                right-=1
19
20        return operation
21
22
23         
24        
25        