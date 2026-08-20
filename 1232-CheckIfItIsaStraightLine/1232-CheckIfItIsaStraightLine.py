# Last updated: 20/08/2026, 14:12:07
1class Solution:
2    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
3        if len(coordinates) <= 2:
4            return True
5
6        x0, y0 = coordinates[0]  # First point
7        x1, y1 = coordinates[1]  # Second point
8
9        dx = x1 - x0
10        dy = y1 - y0
11
12        for i in range(2, len(coordinates)):
13            x,y = coordinates[i]
14
15            left_side = (y-y0)*dx
16            right_side = (x-x0)*dy
17
18            if right_side!=left_side:
19                return False
20
21        return True
22