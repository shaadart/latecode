class Solution:
    def findEquilibrium(self, arr):
        
        rightsum = sum(arr)
        leftsum = 0
        
        for i in range(len(arr)):
            rightsum -= arr[i]
            if leftsum == rightsum:
                return i
            leftsum += arr[i]
            
        return -1
            
            
                
            

