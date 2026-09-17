class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(ch, mov):
            mov = mov % 26
            res = ""

            res = chr((ord(ch) - ord("a") + mov) % 26 + ord("a"))

            return res

        
        res = ""
        for i in range(len(s)):
        
            if s[i].isdigit():
                res+=shift(s[i-1],int(s[i]))
            else: 
                res+=s[i]

        return res
                


   