# Last updated: 19/10/2026, 16:20:56
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        
        ans = float("inf")

        n = len(nums)

        small = SortedList()
        large = SortedList()

        cur_sum = 0
        i = 1

        #make a window

        while i < n and i - dist < 1:
            small.add((nums[i], i))
            cur_sum += nums[i]

            if len(small) > k-1: # k-1 because we already have nums[0]
                val, idx = small.pop()
                cur_sum -= val
                large.add((val,idx))

            if len(small) == k-1:
                ans = min(cur_sum, ans)
            
            i+=1

        


        #Sliding the Window

        #lets say k = 3, dist = 2 then i is at 2nd index i.e 8 so we are going till end and remove and add shit acccordingly

        while i < n:
            # add new element
            small.add((nums[i], i))
            cur_sum += nums[i]

            if len(small) > k - 1:
                val, idx = small.pop()
                cur_sum -= val
                large.add((val, idx))

            if len(small) == k-1:
                ans = min(cur_sum, ans)

            # remove expired element (THIS WAS WRONG)
            remove = (nums[i - dist], i - dist)

            if remove in small:
                small.remove(remove)
                cur_sum -= remove[0]

                if large:
                    val, idx = large.pop(0)
                    small.add((val, idx))
                    cur_sum += val
            elif remove in large:
                large.remove(remove)

            


            i += 1




        return nums[0] + ans











        

        