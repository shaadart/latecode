from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        n = len(positions)
        indices = sorted(range(n), key=lambda i: positions[i])

        stack = []

        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    j = stack.pop()

                    if healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                        stack.append(j)

                    elif healths[j] < healths[i]:
                        healths[i] -= 1
                        healths[j] = 0

                    else:  # equal health
                        healths[i] = 0
                        healths[j] = 0

        # collect survivors
        result = []
        for i in range(n):
            if healths[i] > 0:
                result.append(healths[i])

        return result