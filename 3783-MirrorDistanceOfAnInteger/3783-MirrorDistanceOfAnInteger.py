# Last updated: 19/10/2026, 16:18:34
class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            reverse = 0 
            while n != 0:
                digit = n % 10
                reverse = (reverse*10) + digit 
                n = n // 10

            return reverse

        return abs(reverse(n) - n)


        