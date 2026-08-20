# Last updated: 20/08/2026, 13:20:19
1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        i,j = 0,0
4        merged = []
5        while i < len(word1) and j < len(word2):
6            merged.append(word1[i])
7            merged.append(word2[j])
8            i += 1
9            j += 1
10
11        if i < len(word1):
12            merged.append(word1[i:])
13        if j < len(word2):
14            merged.append(word2[j:])
15
16        return "".join(merged)
17