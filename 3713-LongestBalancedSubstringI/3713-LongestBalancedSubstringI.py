# Last updated: 19/10/2026, 16:18:55
# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         n = len(nums)

#         i = 0
#         maxlen = 0

#         for j in range(n):
#             while i <= j and nums[j] > k * nums[i]:
#                 i += 1
#             maxlen = max(maxlen, j - i + 1)

#         return n - maxlen


# class Solution:
#     def longestBalanced(self, nums: List[int]) -> int:
#         n = len(nums)
#         maxlen = 0

#         for i in range(n):
#             even_set = set()
#             odd_set = set()

#             for j in range(i, n):
#                 if nums[j] % 2 == 0:
#                     even_set.add(nums[j])
#                 else:
#                     odd_set.add(nums[j])

#                 if len(even_set) == len(odd_set):
#                     maxlen = max(maxlen, j - i + 1)

#         return maxlen



class Solution:


    def all_values_equal(d):
        """Checks if all values in the dictionary d are equal."""
        if not d:
            return True # An empty dictionary can be considered as having all values equal
        return len(set(d.values())) == 1

    def longestBalanced(self, s: str) -> int:
        maxlen = 0
        n = len(s)
        for i in range(n):

            freq = {}
            values_list = []

            for j in range(i,n):
                freq[s[j]] = freq.get(s[j], 0) + 1

                values = freq.values()


                if len(set(values)) == 1:
                    maxlen = max(maxlen, j - i + 1)  

        return maxlen

        