class Solution:
    def subarraySum(self, arr, target):
        if not arr:
            return [-1]
            
        n = len(arr)
        i = 0
        j = 0
        tot = arr[0]

        while j < n:
            if tot == target:
                return [i+1, j+1]
                
            elif tot > target: 
                
                tot -= arr[i]
                i += 1
        
                if i < n and i > j: 
                    j = i
                    tot = arr[i]
                    
            else: 
                j += 1
                if j == n:
                    break
                tot += arr[j]
                
                
        return [-1]
                
                
                
    #             class Solution:
    # def subarraySum(self, arr, target):
    #     n = len(arr)
    #     i = 0
    #     j = 0
    #     tot = arr[0]

    #     while j < n:
    #         if tot == target:
    #             return [i + 1, j + 1]

    #         elif tot < target:
    #             j += 1
    #             if j == n:
    #                 break
    #             tot += arr[j]

    #         else:
    #             tot -= arr[i]
    #             i += 1

    #             if i > j and i < n:
    #                 j = i
    #                 tot = arr[i]

    #     return [-1]
                
                
                
                
                