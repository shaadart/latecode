# Last updated: 21/08/2026, 07:45:57
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        seeni = {}
4        seenj = {}
5
6        for i in s: 
7            seeni[i] = seeni.get(i, 0)+1
8
9        for j in t: 
10            seenj[j] = seenj.get(j, 0)+1
11
12        return seenj == seeni
13
14        
15
16        