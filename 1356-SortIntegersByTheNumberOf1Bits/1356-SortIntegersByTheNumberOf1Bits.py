# Last updated: 19/10/2026, 16:24:40
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        seen = {}
        l = len(arr)
        ans = []

        arr.sort()

        for i in range(l):
            count = bin(arr[i]).count("1")
            if count not in seen:
                seen[count] = []
            seen[count].append(arr[i])


        for count in sorted(seen):
            ans.extend(seen[count])

        return ans
        

        
        
