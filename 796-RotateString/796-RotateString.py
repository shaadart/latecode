# Last updated: 19/10/2026, 16:26:07
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s)==len(goal) and (s+s).find(goal)!=-1
        