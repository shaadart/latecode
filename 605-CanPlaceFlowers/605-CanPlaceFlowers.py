# Last updated: 19/10/2026, 16:26:56
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_khali = (i == 0) or (flowerbed[i-1] == 0)
                right_khali = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)

                if left_khali and right_khali:
                    flowerbed[i] = 1   # place a flower
                    n -= 1
                    if n == 0:
                        return True
        
        return n == 0