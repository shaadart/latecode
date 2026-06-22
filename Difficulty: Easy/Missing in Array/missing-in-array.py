class Solution:
    def missingNum(self, arr):
        arr.sort()
        
        
        if arr[0] != 1:
            return 1
        
        for i in range(1, len(arr)):
            
            if arr[i] - arr[i-1] != 1:
                return arr[i-1]+1
                
            
        return arr[-1]+1
            
                