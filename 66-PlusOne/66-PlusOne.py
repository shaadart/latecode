# Last updated: 3/30/2026, 10:42:13 AM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3
4     
5
6        for i in range(len(digits)-1, -1, -1):
7            if digits[i] + 1 != 10:
8                digits[i] +=1
9                return digits
10
11            digits[i] =0
12
13            if i == 0:
14                return [1]+digits
15
16
17
18
19
20        