class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        

        n = len(nums)
        k %= n 
        l = nums[:n-k]
        r = nums[n-k:]
        nums[:] = r+l
            
        