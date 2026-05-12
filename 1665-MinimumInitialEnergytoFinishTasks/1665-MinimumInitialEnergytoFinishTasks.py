# Last updated: 5/13/2026, 12:57:47 AM
1class Solution:
2    def minimumEffort(self, shop: list[list[int]]) -> int:
3        shop.sort(key=lambda x: x[1] - x[0], reverse=True)
4
5        def test(bal):
6            for cost, thresh in shop:
7                if bal < thresh:
8                    return False
9                bal -= cost
10            return True
11
12        return bisect.bisect_left(range(10**9 + 1), True, key=test)
13