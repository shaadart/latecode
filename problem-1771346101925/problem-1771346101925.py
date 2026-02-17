# Last updated: 2/17/2026, 10:05:01 PM
1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        res = []
4        
5        for i in range (12): 
6            for j in range (60):
7
8                if (bin(i).count('1') + bin(j).count('1')) == turnedOn:
9                    time = f"{i}:{j:02}"
10                    res.append(time)
11
12        return res