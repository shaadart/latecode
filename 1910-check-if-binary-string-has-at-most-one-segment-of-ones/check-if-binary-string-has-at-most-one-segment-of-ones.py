class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        count = 0 
        n = len(s)
        i = 0

        while i < n:

            if s[i] == '1':
                count+=1
                while i < n and s[i] == "1":
                    i+=1

            else: 
                i+=1

        
        if count == 1:
            return True

        return False


        