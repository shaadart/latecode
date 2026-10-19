# Last updated: 19/10/2026, 16:27:52
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num        # smallest so far
            elif num <= second:
                second = num       # second smallest
            else:
                return True        # found num > first and second
        
        return False
