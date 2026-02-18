# Last updated: 2/18/2026, 7:06:58 PM
1# class Solution:
2#     def hasAlternatingBits(self, n: int) -> bool:
3#         original_bit = format(n, 'b')
4#         rang = len(original_bit)
5#         bity = int(original_bit)
6#         res = False
7
8#         for i in range(rang):
9            
10#             gone = bity & 1
11#             shift = gone >> 1
12#             print(rang, i, gone, shift)
13#             if gone != (shift & 1):
14#                 bity >>= 1
15#                 res == True
16
17#             else:
18#                 return False
19       
20#         return res
21        
22
23class Solution:
24    def hasAlternatingBits(self, n: int) -> bool:
25        prev = n & 1 
26        n >>= 1
27        print(n, prev)
28        while n: 
29            curr = n & 1
30            if curr == prev: 
31                return False
32            
33            prev = curr
34            n >>=1 
35
36        
37        return True
38            