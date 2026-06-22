class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        
        total = arr[0]
        maintotal = total
        for i in range(1, len(arr)):
            if total<0:
                total = arr[i]
            else: 
                total+=arr[i]
                
            
            maintotal = max(maintotal, total)
            
            
        return maintotal
                
            
        