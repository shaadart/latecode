class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        i = 1
        stk = [nums[0]]
        while i < len(nums) and nums[i] == stk[-1]+1:
            stk.append(nums[i])
            i+=1
            

        tot = sum(stk)

        print(tot)

        while tot in nums:
            tot+=1

        return tot




        