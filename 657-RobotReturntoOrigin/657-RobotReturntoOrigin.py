# Last updated: 21/08/2026, 08:34:12
1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3
4        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')
5