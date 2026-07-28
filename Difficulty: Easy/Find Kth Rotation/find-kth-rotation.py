class Solution:
    def findKRotation(self, arr):
        # The index of the minimum element tells you the rotation count
        return arr.index(min(arr))
