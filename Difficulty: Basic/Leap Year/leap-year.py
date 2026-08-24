class Solution:
    def checkYear (self, n):
        def isleap(i):
            if i % 400 == 0 or (i%4 == 0 and i%100 != 0):
                return True
            return False
            
        return isleap(n)
        # code here
        