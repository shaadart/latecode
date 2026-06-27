class Solution:
    def majorityElement(self, arr):
        #code here
        
        out = {}
        
        for i in range(len(arr)):
            out[arr[i]] = out.get(arr[i], 0) + 1
            
        
        for idx, (key, value) in enumerate(out.items()):
            if value>(len(arr)/2):
                return key
                
            else:
                continue
            
        return -1
