# Last updated: 3/14/2026, 8:40:57 PM
1# Added using AI
2class Solution:
3    def getHappyString(self, n: int, k: int) -> str:
4        sz = 2 ** (n - 1)
5        if 3 * sz < k:
6            return ""
7
8        opts = ["bc", "ac", "ab"]
9        if k <= sz:         res = "a"
10        elif k <= 2 * sz:   res = "b"; k -= sz
11        else:               res = "c"; k -= 2 * sz
12
13        for i in range(1, n):
14            sz //= 2
15            ch = opts[ord(res[-1]) - ord('a')]
16            if k <= sz: res += ch[0]
17            else:       res += ch[1]; k -= sz
18
19        return res