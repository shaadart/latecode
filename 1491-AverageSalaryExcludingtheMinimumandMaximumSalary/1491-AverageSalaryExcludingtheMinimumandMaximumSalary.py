# Last updated: 20/08/2026, 12:12:19
1class Solution:
2    def average(self, salary: List[int]) -> float:
3        salary.remove(max(salary))
4        salary.remove(min(salary))
5        return sum(salary)/len(salary)
6        