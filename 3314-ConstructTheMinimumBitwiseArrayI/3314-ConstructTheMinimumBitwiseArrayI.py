# Last updated: 19/10/2026, 16:20:38
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            found = False



            for j in range(0, nums[i]):
                if((j | j+1) == nums[i]):
                    res.append(j)
                    found = True
                    break
            if found == False: 
                res.append(-1)

        return res

            

                


        