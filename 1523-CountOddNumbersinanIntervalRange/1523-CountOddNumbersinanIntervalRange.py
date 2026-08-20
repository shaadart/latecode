# Last updated: 20/08/2026, 18:01:28
1class Solution:
2    def countOdds(self, low: int, high: int) -> int:
3        # Total numbers in the range [low, high]
4        total_numbers = high - low + 1
5        
6        if low % 2 == 0:
7            return total_numbers // 2
8        else:
9            return (total_numbers + 1) // 2