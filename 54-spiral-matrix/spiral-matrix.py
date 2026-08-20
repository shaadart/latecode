class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        total = rows*cols
        counter = 0 
        out = []

        while counter < total : 
            for i in range(left, right+1):
                out.append(matrix[top][i])
                counter +=1

            top+=1
            if counter >= total:
                break

            for i in range(top, bottom+1):
                out.append(matrix[i][right])
                counter+=1

            right-=1
            if counter >= total:
                break

            for i in range(right, left-1,-1):
                out.append(matrix[bottom][i])
                counter+=1
            
            bottom-=1

            if counter >= total:
                break

            for i in range(bottom, top-1, -1):
                out.append(matrix[i][left])
                counter+=1

            left+=1



        return out
                




        