# Last updated: 05/08/2026, 12:39:26
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4
5        answer = [intervals[0]]
6
7        for current in intervals[1:]:
8
9            previous = answer[-1]
10
11            if current[0] <= previous[1]:
12                previous[1] = max(previous[1], current[1])
13
14            else:
15                answer.append(current)
16
17        return answer