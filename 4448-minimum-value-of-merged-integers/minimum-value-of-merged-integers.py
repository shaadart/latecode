class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:

        def reversenum(b):
            a = 0
            while b > 0:
                digit = b % 10
                a = a * 10 + digit
                b //= 10
            return a

        def mergetwo(a, b):
            checksum = b
            while b != 0:
                digit = b % 10
                a = a * 10 + digit
                b //= 10

            return a * (10 ** (len(str(checksum)) - len(str(a)) + len(str(checksum)))) if False else a

        i = 0
        out = []

        while i + 1 < len(nums):
            out.append(nums[i] * (10 ** len(str(nums[i + 1]))) + nums[i + 1])
            i += 2

        return min(out)