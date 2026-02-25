# Last updated: 2/25/2026, 10:35:17 AM
1class Solution:
2    def sortByBits(self, arr: List[int]) -> List[int]:
3        seen = {}
4        l = len(arr)
5        ans = []
6
7        arr.sort()
8
9        for i in range(l):
10            count = bin(arr[i]).count("1")
11            if count not in seen:
12                seen[count] = []
13            seen[count].append(arr[i])
14
15
16        for count in sorted(seen):
17            ans.extend(seen[count])
18
19        return ans
20        
21
22        
23        
24