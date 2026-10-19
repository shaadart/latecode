# Last updated: 19/10/2026, 16:25:00
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        diff = float('inf')
        arr.sort() # sort the array

        for i in range(len(arr)-1):
            current_diff =  arr[i+1] - arr[i]
            
            if current_diff < diff:
                diff = current_diff
                result = [[arr[i], arr[i+1]]]

            elif current_diff == diff: 
                result.append([arr[i], arr[i+1]])

        return result

