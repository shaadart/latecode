class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        times = k
        n = len(nums)
        i = 0
        section = nums[i : i + k]
        avgsum = sum(section)
        res = avgsum / times

        while i + k < n:
            
            avgsum = avgsum -nums[i] + nums[i+k]
            res = max(res, avgsum / times)

            i += 1

        return res

        # for i in range(times):

        #     out.append(nums.pop(nums.index(max(nums))))
        #     print(out)
        #     times-=1

        # return sum(out)/k
