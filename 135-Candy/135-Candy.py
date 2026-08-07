# Last updated: 07/08/2026, 11:21:33
1class Solution:
2    def candy(self, ratings: List[int]) -> int:
3
4        n = len(ratings)
5        candies = n * [1]
6
7        #left to right
8        for i in range(1,n):
9            if ratings[i] > ratings[i-1]:
10                candies[i] = candies[i-1]+1
11
12        #right to left
13        for i in range(n-2, -1, -1):
14            if ratings[i] > ratings[i+1]:
15                candies[i] = max(candies[i], candies[i+1]+1)
16
17        return sum(candies)
18        