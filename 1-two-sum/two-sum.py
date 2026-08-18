class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Changed from a set() to a dictionary to store {value: index}
        seen = {} 
        n = len(nums)
        
        for i in range(n):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i          