class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        out = []

        if n % 2 == 0:
            for i in range(n):

                for j in range(n):

                    if i == j:
                        out.append(mat[i][j])

            r, c = 0, n - 1
            while c >= 0 and r < n:
                out.append(mat[r][c])

                r += 1
                c -= 1

        else:
            for i in range(n):

                for j in range(n):

                    if i == j:
                        out.append(mat[i][j])

            r, c = 0, n - 1

            while c >= 0 and r < n:
                if r == c:
                    r += 1
                    c -= 1
                    continue  

                out.append(mat[r][c])
                
                r += 1
                c -= 1


            

        return sum(out)
