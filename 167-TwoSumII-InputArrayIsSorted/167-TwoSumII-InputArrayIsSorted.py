# Last updated: 19/11/2026, 07:21:44
1class Solution:
2    def twoSum(self, numbers: list[int], target: int) -> list[int]:
3        left = 0
4        right = len(numbers)-1
5
6        while left < right:
7            if numbers[left] + numbers[right] > target:
8                right-=1
9
10            elif numbers[left] + numbers[right] < target:
11                left+=1
12
13            else:
14                return [left+1, right+1]
15
16
17
18
19
20        