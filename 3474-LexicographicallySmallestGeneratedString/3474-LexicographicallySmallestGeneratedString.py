# Last updated: 3/31/2026, 3:27:02 PM
1class Solution:
2    def generateString(self, str1: str, str2: str) -> str:
3        n, m = len(str1), len(str2)
4        N = n + m - 1 
5
6        word = ['#'] * N
7        can_change = [False] * N
8
9        #Processing te T:
10
11        for i in range(n):
12            if str1[i] == "T":
13                for j in range(m):
14                    if word[i+j] != '#' and word[i+j] != str2[j]:
15                        return ""
16
17                    word[i+j] = str2[j]   
18
19        # filling a
20
21        for i in range(N):
22            if word[i] == "#":
23                word[i] = 'a'
24                can_change[i] = True
25
26        #helper function
27        def is_same(i):
28            return word[i:i+m] == list(str2)
29
30        # Processfigng F
31
32        for i in range(n):
33            if str1[i] == "F":
34                if is_same(i):
35                    changed = False
36
37                    for k in range(i+m-1, i-1, -1): 
38                        
39                        #reading it backwards bcs we need to find lexicographically smallest output so changing staring ones we will mess the shit up 
40
41                        if can_change[k]:
42                            word[k] = "b"
43                            changed = True
44                            break
45
46                    if not changed:
47                        return ""
48
49        return "".join(word)