class Solution:
    def minOperations(self, s: str) -> int:

        n = len(s)

        startw0 = 0  # 01010101..
        startw1 = 0  # 10101010..

        for i in range(n):
            if i % 2 == 0:
                if s[i] != '0':
                    startw0 += 1
                if s[i] != '1':
                    startw1 += 1
            else:
                if s[i] != '1':
                    startw0 += 1
                if s[i] != '0':
                    startw1 += 1

        return min(startw0, startw1)