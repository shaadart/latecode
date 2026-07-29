class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        
        # Edge case: Single element is always a peak
        if n == 1:
            return 0 
            
        # Edge case: Check the first element
        if arr[0] >= arr[1]:
            return 0
            
        # Edge case: Check the last element
        if arr[n-1] >= arr[n-2]:
            return n - 1
            
        # Check internal elements
        def check(arr, a, b, c):
            if arr[a] <= arr[b] and arr[b] >= arr[c]:
                return True
            return False
                
        i, j, k = 0, 1, 2
        while k < n:
            if check(arr, i, j, k):
                return j  # Return the index of the peak element
            i += 1
            j += 1
            k += 1
                
        return -1
