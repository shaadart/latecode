# Last updated: 19/10/2026, 16:23:57
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        last_el = arr[-1]
        missing_list = []

        for i in range(1,last_el+1 + k):
            if i not in arr:
                missing_list.append(i)

            if len(missing_list) == k:
                    return missing_list[-1]


