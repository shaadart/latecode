class Solution:
    def modify(self, s):
        vowels = "aeiou"
        s = list(s)

        left = 0
        right = len(s) - 1
        
        s = list(s)

        while left < right:
            if s[left] in vowels:
                
                while left < right and s[right] not in vowels:
                    right-=1
                    
                if left < right:
                    s[right], s[left] = s[left], s[right]
                    right -= 1
                    
                left+=1
                    
                    
            else: 
                left+=1
                
                
        return "".join(s)
                
     
                    
                    
            
                
            
            