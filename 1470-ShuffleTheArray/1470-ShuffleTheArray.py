# Last updated: 19/10/2026, 16:24:14
class Solution(object):
    def shuffle(self, nums, n):
        # split 
        #one loop that will run
        #    - till first split
        #    - till the end 

        # or...
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])

        return ans
        