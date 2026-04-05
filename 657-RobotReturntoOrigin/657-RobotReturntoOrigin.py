# Last updated: 4/6/2026, 12:17:09 AM
1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        if len(moves) & 1: return False
4        x = y = 0
5
6        for c in moves:
7            y += (c == 'U') - (c == 'D')
8            x += (c == 'R') - (c == 'L')
9
10        return not x and not y