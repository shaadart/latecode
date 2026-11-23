# Last updated: 23/11/2026, 11:34:05
1class Solution:
2    def minMergedInteger(self, nums: list[int]) -> int:
3
4        def reversenum(b):
5            a = 0
6            while b > 0:
7                digit = b % 10
8                a = a * 10 + digit
9                b //= 10
10            return a
11
12        def mergetwo(a, b):
13            checksum = b
14            while b != 0:
15                digit = b % 10
16                a = a * 10 + digit
17                b //= 10
18
19            return a * (10 ** (len(str(checksum)) - len(str(a)) + len(str(checksum)))) if False else a
20
21        i = 0
22        out = []
23
24        while i + 1 < len(nums):
25            out.append(nums[i] * (10 ** len(str(nums[i + 1]))) + nums[i + 1])
26            i += 2
27
28        return min(out)