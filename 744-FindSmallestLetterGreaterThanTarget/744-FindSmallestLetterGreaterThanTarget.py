# Last updated: 19/10/2026, 16:27:06
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target = ord(target)
        nums = [ord(c) for c in letters]

        for n in nums:
            if n > target:
                return chr(n)

        return chr(nums[0])   
