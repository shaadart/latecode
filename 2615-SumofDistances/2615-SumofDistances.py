# Last updated: 4/24/2026, 12:23:00 AM
1class Solution:
2    def distance(self, nums: List[int]) -> List[int]:
3        
4        n = len(nums)
5        count_right = dict()
6        count_left = dict()
7        lastseen_right = dict()
8        lastseen_left = dict()
9        prefixsum_right = [0]*n
10        prefixsum_left = [0]*n
11        for i in range(n):
12            #Right part i.e. processing left to right
13            num=nums[i]
14            if num in lastseen_right:
15                lastseen_idx = lastseen_right[num]
16                prefixsum_right[i] = prefixsum_right[lastseen_idx]+lastseen_right[num]
17            lastseen_right[num]=i
18
19            #Left part i.e. processing right to left
20            i=n-1-i
21            num=nums[i]
22            if num in lastseen_left:
23                lastseen_idx = lastseen_left[num]
24                prefixsum_left[i] = prefixsum_left[lastseen_idx]+lastseen_left[num]
25            lastseen_left[num]=i
26
27        arr = [0]*n
28        for i in range(n):
29            #calculating and adding for right part
30            num = nums[i]
31            if num in count_right:
32                arr[i] += (i*count_right[num])-prefixsum_right[i]
33                count_right[num]+=1
34            
35            else:
36                count_right[num]=1
37            #calculating and adding for left part
38            i=n-1-i
39            num = nums[i]
40            if num in count_left:
41                arr[i] += prefixsum_left[i]-(i*count_left[num])
42                count_left[num]+=1
43            
44            else:
45                count_left[num]=1
46        
47        return arr