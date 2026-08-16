class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #sort
        
        out = []
        #count and store 
        groups = {}

        for i in nums:
            if i in groups:  
                groups[i] = groups.get(i) + 1
            else: 
                groups[i] = 1

        print(groups)

        
        #extract k times highest oness
        while k != 0:
            highest_key = max(groups, key=groups.get) #1

            out.append(highest_key)
            groups.pop(highest_key,None)      
            k-=1

        return out
