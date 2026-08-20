class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        countzero = 0
        temp = []

        for i in nums:
            if i == 0:
                continue
            else:
                temp.append(i)

        trun = len(nums)-len(temp)

        for i in range(trun):
            temp.append(0)

        nums[:] = temp