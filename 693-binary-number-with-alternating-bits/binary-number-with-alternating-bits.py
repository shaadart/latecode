# class Solution:
#     def hasAlternatingBits(self, n: int) -> bool:
#         original_bit = format(n, 'b')
#         rang = len(original_bit)
#         bity = int(original_bit)
#         res = False

#         for i in range(rang):
            
#             gone = bity & 1
#             shift = gone >> 1
#             print(rang, i, gone, shift)
#             if gone != (shift & 1):
#                 bity >>= 1
#                 res == True

#             else:
#                 return False
       
#         return res
        

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1 
        n >>= 1
        print(n, prev)
        while n: 
            curr = n & 1
            if curr == prev: 
                return False
            
            prev = curr
            n >>=1 

        
        return True
            