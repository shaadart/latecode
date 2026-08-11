class Solution:
    def getSecondLargest(self, arr):
        
        nums = list(set(arr))
        
        if len(nums) < 2: 
            return -1
    
        nums.sort()
        return nums[-2]
        # code here
        