# Last updated: 19/10/2026, 16:25:28
def find_distance(a,b):
    return max(abs(a[1] - b[1]), abs(a[0]-b[0]))


class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        distance = 0




        for i in range(len(points)-1):
            distance += find_distance(points[i], points[i+1])


        return distance

        