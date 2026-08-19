class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        diff = arr[1] - arr[0]
        i = 1
        n = len(arr)
        while i < n:
            if arr[i] - arr[i-1] == diff:
                i+=1
                continue

            else:
                return False

        return True


        