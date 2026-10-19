# Last updated: 19/10/2026, 16:23:59
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Total numbers in the range [low, high]
        total_numbers = high - low + 1
        
        if low % 2 == 0:
            return total_numbers // 2
        else:
            return (total_numbers + 1) // 2