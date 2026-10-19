# Last updated: 19/10/2026, 16:21:23
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        count_right = dict()
        count_left = dict()
        lastseen_right = dict()
        lastseen_left = dict()
        prefixsum_right = [0]*n
        prefixsum_left = [0]*n
        for i in range(n):
            #Right part i.e. processing left to right
            num=nums[i]
            if num in lastseen_right:
                lastseen_idx = lastseen_right[num]
                prefixsum_right[i] = prefixsum_right[lastseen_idx]+lastseen_right[num]
            lastseen_right[num]=i

            #Left part i.e. processing right to left
            i=n-1-i
            num=nums[i]
            if num in lastseen_left:
                lastseen_idx = lastseen_left[num]
                prefixsum_left[i] = prefixsum_left[lastseen_idx]+lastseen_left[num]
            lastseen_left[num]=i

        arr = [0]*n
        for i in range(n):
            #calculating and adding for right part
            num = nums[i]
            if num in count_right:
                arr[i] += (i*count_right[num])-prefixsum_right[i]
                count_right[num]+=1
            
            else:
                count_right[num]=1
            #calculating and adding for left part
            i=n-1-i
            num = nums[i]
            if num in count_left:
                arr[i] += prefixsum_left[i]-(i*count_left[num])
                count_left[num]+=1
            
            else:
                count_left[num]=1
        
        return arr