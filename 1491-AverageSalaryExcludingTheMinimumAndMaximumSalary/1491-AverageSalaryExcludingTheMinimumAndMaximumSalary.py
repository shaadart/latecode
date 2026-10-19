# Last updated: 19/10/2026, 16:24:46
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary)/len(salary)
        