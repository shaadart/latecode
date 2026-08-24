class Solution:
    def sieve(self, n):
        res = []
        
        def isprime(k):
            for i in range(2, int(k**0.5)+1):
                if k % i == 0:
                    return False
            return True
                
        for i in range(2, n+1):
            
            if isprime(i):
                res.append(i)
                
        return res
                    
                
