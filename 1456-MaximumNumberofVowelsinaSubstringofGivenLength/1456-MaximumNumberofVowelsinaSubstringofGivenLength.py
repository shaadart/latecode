# Last updated: 23/08/2026, 21:48:40
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        i = 0
4        n = len(s)
5
6        ans = 0
7        count = 0
8
9
10        for i in range(k):
11            if s[i] in "aeiou":
12                count += 1
13
14        ans = count
15
16        for j in range(k, n):
17            if s[j] in "aeiou":
18                count += 1
19
20            if s[j - k] in "aeiou":
21                count -= 1
22
23            ans = max(count, ans)
24
25        return ans
26