# Last updated: 4/22/2026, 10:59:46 AM
1class Solution:
2    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
3        res = []
4        
5        for q in range(len(queries)):
6            for d in range(len(dictionary)):
7                diff = 0
8                
9                for j in range(len(queries[0])):
10                    if queries[q][j] != dictionary[d][j]:
11                        diff += 1
12                        if diff > 2:
13                            break
14                
15                if diff <= 2:
16                    res.append(queries[q])
17                    break        
18        return res