# Last updated: 19/10/2026, 16:24:19
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum_number_candies = max(candies)
        fin_list = []
        for i in range(len(candies)):


            if candies[i]+extraCandies >= maximum_number_candies:
                fin_list.append(True)
            else:
                fin_list.append(False)

        return fin_list



        