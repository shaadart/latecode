class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 1

        for i in range(1, n+1):
            res*=i

        cz = 0 

        while res > 0 and res%10==0:
            cz+=1
            res//=10

        return cz


        