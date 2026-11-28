# Last updated: 28/11/2026, 12:24:12
1class Solution:
2    def findMaxAverage(self, nums: list[int], k: int) -> float:
3
4        times = k
5        n = len(nums)
6        i = 0
7        section = nums[i : i + k]
8        avgsum = sum(section)
9        res = avgsum / times
10
11        while i + k < n:
12            
13            avgsum = avgsum -nums[i] + nums[i+k]
14            res = max(res, avgsum / times)
15
16            i += 1
17
18        return res
19
20        # for i in range(times):
21
22        #     out.append(nums.pop(nums.index(max(nums))))
23        #     print(out)
24        #     times-=1
25
26        # return sum(out)/k
27