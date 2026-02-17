# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         maxCount = 1

#         for i in range(len(nums)):
#             curCount = nums.count(nums[i])
#             if (curCount > maxCount):
#                 maxCount = curCount
#             elif (curCount == maxCount and maxCount > 1):
#                 maxCount += curCount

#             else:
#                 continue

#         if maxCount == 1: 
#             print("this is triggered")
#             return len(nums)

#         else: 
#             return maxCount

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxFreq = 0
        total = 0
        seen = []   # track processed numbers

        for i in range(len(nums)):
            if nums[i] in seen:
                continue

            curFreq = nums.count(nums[i])
            seen.append(nums[i])

            if curFreq > maxFreq:
                maxFreq = curFreq
                total = curFreq
            elif curFreq == maxFreq:
                total += curFreq

        return total
