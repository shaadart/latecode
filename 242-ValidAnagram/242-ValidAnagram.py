# Last updated: 4/27/2026, 12:50:16 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        #sort
4        nums.sort()
5        out = []
6        
7        #count and store 
8        groups = {}
9
10        for i in nums:
11            if i in groups:  
12                groups[i] = groups.get(i) + 1
13            else: 
14                groups[i] = 1
15
16        
17        #extract k times highest oness
18        while k != 0:
19            highest_key = max(groups, key=groups.get) #1
20            out.append(highest_key)
21            groups.pop(highest_key,None)      
22            k-=1
23
24        return out
25