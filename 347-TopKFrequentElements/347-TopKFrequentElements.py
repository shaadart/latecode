# Last updated: 16/08/2026, 11:43:49
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        #sort
4        
5        out = []
6        #count and store 
7        groups = {}
8
9        for i in nums:
10            if i in groups:  
11                groups[i] = groups.get(i) + 1
12            else: 
13                groups[i] = 1
14
15        print(groups)
16
17        
18        #extract k times highest oness
19        while k != 0:
20            highest_key = max(groups, key=groups.get) #1
21
22            out.append(highest_key)
23            groups.pop(highest_key,None)      
24            k-=1
25
26        return out
27