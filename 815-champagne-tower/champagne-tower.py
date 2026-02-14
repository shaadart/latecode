class Solution:

    

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        t = [[0,0] * 101 for _ in range(101)] # this shit will create 101 x 101 matrix
        t[0][0] = float(poured)

        for row in range(query_row + 1):
            for col in range (row+1):
                extra = (t[row][col] -1 ) / 2.0
                if extra > 0: 
                    t[row+1][col] += extra 
                    t[row+1][col+1] += extra 



        return min(1.0,t[query_row][query_glass])


        