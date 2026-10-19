# Last updated: 19/10/2026, 16:27:58
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #store in dick
        freq = {}
        n = len(nums)
        for i in range(n):
            # if freq[nums[i]].get()
             freq[nums[i]] = freq.get(nums[i], 0) + 1

        return max(freq, key=freq.get)
        