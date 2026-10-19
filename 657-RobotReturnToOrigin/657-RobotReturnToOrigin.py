# Last updated: 19/10/2026, 16:26:44
class Solution:
    def judgeCircle(self, moves: str) -> bool:

        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')
