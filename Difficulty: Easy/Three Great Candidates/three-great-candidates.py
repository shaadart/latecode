import math

class Solution:
    def maxProduct(self, arr):
        arr.sort()
    # Opion 1: Product of the three largest numbers
    # Option 2: Product of the two smallest (negative) numbers and the largest number
        return max(arr[-1] * arr[-2] * arr[-3], arr[0] * arr[1] * arr[-1])
        