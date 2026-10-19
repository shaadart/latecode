# Last updated: 19/10/2026, 16:19:01
class Solution: #dint did on my own :(
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        
        if z == 0:
            return 0
        if n == k:
            return 1 if z == n else -1

        b = n - k
        k1 = (z + k - 1) // k
        res = float('inf')
        
        # Case 1: x is Odd
        if (k & 1) == (z & 1):
            t = (n - z + b - 1) // b
            res = max(k1, t) | 1

        # Case 2: x is Even
        if (z & 1) == 0:
            t = (z + b - 1) // b
            e = max(k1, t)
            e += e & 1
            if e < res:
                res = e

        return -1 if res == float('inf') else res

