# Last updated: 19/10/2026, 16:34:10
class Solution:
    def maxArea(self, height: List[int]) -> int:
        final_area = 0
        n = len(height)
        i = 0
        j=n-1

        while(i<j):
            w = j-i
            h = min(height[i], height[j])
            area = w*h
            final_area = max(final_area, area)

            if(height[i]>height[j]):
                j=j-1
            else:
                i = i+1
                

        return final_area

        