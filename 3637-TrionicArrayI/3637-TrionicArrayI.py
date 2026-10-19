# Last updated: 19/10/2026, 16:19:45
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

      
        n = len(nums)
        i = 0
     
       

       #is Increasing
        
        while i+1 < n and nums[i] < nums[i+1]:
            i+=1

        if(i==n-1 or i==0):
            return False

        # is Decreasing

        while i+1 < n and nums[i] > nums[i+1]:
            i+=1

        if(i==n-1):
            return False

        #is Increasing (again)haha 
        
        while i+1 < n and nums[i] < nums[i+1]:
            i+=1

            
        return i==n-1
            
                



                

