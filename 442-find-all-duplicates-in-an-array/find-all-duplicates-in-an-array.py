class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        out = []

        for i in range(len(nums)):
            if nums[i] in seen:
                out.append(nums[i])

            else:
                seen.add(nums[i])

        return out