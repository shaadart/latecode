# Last updated: 17/09/2026, 23:55:28
1class Solution:
2    def replaceDigits(self, s: str) -> str:
3        def shift(ch, mov):
4            mov = mov % 26
5            res = ""
6
7            res = chr((ord(ch) - ord("a") + mov) % 26 + ord("a"))
8
9            return res
10
11        
12        res = ""
13        for i in range(len(s)):
14        
15            if s[i].isdigit():
16                res+=shift(s[i-1],int(s[i]))
17            else: 
18                res+=s[i]
19
20        return res
21                
22
23
24   