class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        answer = [intervals[0]]

        for current in intervals[1:]:

            previous = answer[-1]

            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])

            else:
                answer.append(current)

        return answer