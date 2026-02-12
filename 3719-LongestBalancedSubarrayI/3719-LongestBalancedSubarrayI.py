# Last updated: 2/12/2026, 9:45:00 AM
1# class Solution:
2#     def minRemoval(self, nums: List[int], k: int) -> int:
3#         nums.sort()
4#         n = len(nums)
5
6#         i = 0
7#         maxlen = 0
8
9#         for j in range(n):
10#             while i <= j and nums[j] > k * nums[i]:
11#                 i += 1
12#             maxlen = max(maxlen, j - i + 1)
13
14#         return n - maxlen
15
16
17# class Solution:
18#     def longestBalanced(self, nums: List[int]) -> int:
19#         n = len(nums)
20#         maxlen = 0
21
22#         for i in range(n):
23#             even_set = set()
24#             odd_set = set()
25
26#             for j in range(i, n):
27#                 if nums[j] % 2 == 0:
28#                     even_set.add(nums[j])
29#                 else:
30#                     odd_set.add(nums[j])
31
32#                 if len(even_set) == len(odd_set):
33#                     maxlen = max(maxlen, j - i + 1)
34
35#         return maxlen
36
37
38
39class Solution:
40
41
42    def all_values_equal(d):
43        """Checks if all values in the dictionary d are equal."""
44        if not d:
45            return True # An empty dictionary can be considered as having all values equal
46        return len(set(d.values())) == 1
47
48    def longestBalanced(self, s: str) -> int:
49        maxlen = 0
50        n = len(s)
51        for i in range(n):
52
53            freq = {}
54            values_list = []
55
56            for j in range(i,n):
57                freq[s[j]] = freq.get(s[j], 0) + 1
58
59                values = freq.values()
60
61
62                if len(set(values)) == 1:
63                    maxlen = max(maxlen, j - i + 1)  
64
65        return maxlen
66
67        