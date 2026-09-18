class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        def shift(ch, mov):
            res = ""
            mov = mov % 26

            res = chr((ord(ch) - ord('a') + mov) % 26 + ord('a'))

            return res
        
        a = list(s)
        totalshift = 0 
        for i in range(len(s)-1, -1, -1):
            totalshift = (totalshift+shifts[i]) % 26
            a[i] = shift(a[i], totalshift)
            
        return "".join(a)
