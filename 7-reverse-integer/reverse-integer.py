class Solution:
    def reverse(self, x: int) -> int:

        o = x
        isneg = False
        rev = 0

        if x < 0:
            isneg = True
            x = abs(x)

        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x //= 10

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev if isneg == False else (-rev)