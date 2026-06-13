class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(k):
            rem = nums.pop()
            nums.insert(0, rem)

        return nums
        