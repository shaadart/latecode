class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        x0, y0 = coordinates[0]  # First point
        x1, y1 = coordinates[1]  # Second point

        dx = x1 - x0
        dy = y1 - y0

        for i in range(2, len(coordinates)):
            x,y = coordinates[i]

            left_side = (y-y0)*dx
            right_side = (x-x0)*dy

            if right_side!=left_side:
                return False

        return True
