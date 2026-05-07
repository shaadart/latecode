# Last updated: 5/7/2026, 9:02:54 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3
4        #store in dick
5        freq = {}
6        n = len(nums)
7        for i in range(n):
8            # if freq[nums[i]].get()
9             freq[nums[i]] = freq.get(nums[i], 0) + 1
10
11        return max(freq, key=freq.get)
12        