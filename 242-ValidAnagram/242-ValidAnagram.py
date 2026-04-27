# Last updated: 4/27/2026, 12:17:39 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3
4        out = []
5        sortedstrs = strs[:]
6
7        #sort
8        for i in range(len(strs)):
9            sortedstrs[i] = "".join(sorted(strs[i]))
10
11        
12        # for i in range(len(sortedstrs)):
13        #     for j in range():
14        #     if sortedstrs[i] == sortedstrs[i-1]:
15        
16        groups = defaultdict(list)
17
18        for i in range(len(strs)):
19            groups[sortedstrs[i]].append(strs[i])
20
21
22        for key in groups:
23            out.append(groups[key])
24
25        return out
26
27                
28
29        