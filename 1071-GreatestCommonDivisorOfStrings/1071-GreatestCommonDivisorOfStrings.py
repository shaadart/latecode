# Last updated: 19/10/2026, 16:25:19
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenating in different orders gives different results, no common divisor exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find gcd of lengths
        from math import gcd
        length = gcd(len(str1), len(str2))
        
        # Return the substring of that length
        return str1[:length]
