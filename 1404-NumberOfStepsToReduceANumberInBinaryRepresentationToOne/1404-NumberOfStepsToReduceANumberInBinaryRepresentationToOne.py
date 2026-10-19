# Last updated: 19/10/2026, 16:24:34
class Solution:
    def numSteps(self, s: str) -> int:
        def isOdd(n):
            return n % 2 != 0

        rep = int(s, 2)
        counter = 0
        while rep != 1:
            if isOdd(rep):
                rep= rep+1
                counter+=1
            else: 
                rep = rep//2
                counter+=1

        return counter
