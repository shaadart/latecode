# Last updated: 19/10/2026, 16:23:03
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current, highest = 0,0

        for x in gain:
            current+=x
            highest = max(current, highest)

        return highest 
        