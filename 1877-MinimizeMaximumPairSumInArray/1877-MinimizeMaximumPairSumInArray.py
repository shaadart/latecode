# Last updated: 19/10/2026, 16:22:53
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pairs = []
        nums.sort()

        i=0
        j= len(nums)-1

        while i<j:
            curr_pair = nums[i] + nums[j]
            pairs.append(curr_pair)


            i+=1
            j-=1

        return max(pairs)