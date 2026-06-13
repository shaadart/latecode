class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        

        n = len(nums)
        k %= n 
        r = nums[:n-k]
        l = nums[n-k:]
        nums[:] = l+r
            
        