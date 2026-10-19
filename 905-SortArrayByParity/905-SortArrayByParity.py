# Last updated: 19/10/2026, 16:25:46
class Solution(object):
    def sortArrayByParity(self, nums):
        even = []
        odd = []

        for n in nums:
            if n%2==0:
                even.append(n)

            else: 
                odd.append(n)

        
        return even + odd

            
        