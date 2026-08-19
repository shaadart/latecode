class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for i in nums:
            p = p * i

        print(p)
        if p == 0:
            return 0

        elif p >= 0:
            return 1

        elif p<=0:
            return -1
