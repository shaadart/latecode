# Last updated: 19/10/2026, 16:22:21
class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        n = len(nums)

        for i in range(0, n):
            ans.append(nums[i])
            # ans.insert(nums[i], i)
            # ans.insert(nums[i], i+n)
        for i in range(0,n):
            ans.append(nums[i])
        
        return ans
        

# optial solution

# class Solution(object):
#     def getConcatenation(self, nums):
#         return nums + nums
