class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        def getleftmaxarr(height, n):
            left = [0] * n
            left[0] = height[0]
            for i in range(1, n):
                left[i] = max(left[i-1], height[i])
            return left

        def getrightmaxarr(height, n):
            right = [0] * n
            right[n-1] = height[n-1]
            for i in range(n-2, -1, -1):
                right[i] = max(right[i+1], height[i])
            return right

        leftmaxarr = getleftmaxarr(height, n)
        rightmaxarr = getrightmaxarr(height, n)

        sum = 0
        for i in range(1, len(height)):

            trap = min(leftmaxarr[i], rightmaxarr[i]) - height[i]
            sum = sum + trap 

        return sum