class Solution:
    def rotateArr(self, arr, d):
        # code here
        n = len(arr)
        d %= n
        
        r = arr[d:]
        l = arr[:d]
        
        arr[:] = r + l