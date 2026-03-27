class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        def left_rotate(arr, d):
            n = len(arr)
            d = d % n 
            return (arr == (arr[d:] + arr[:d]))

        def right_rotate(arr, d):
            n = len(arr)
            d = d % n 
            return (arr == (arr[-d:] + arr[:-d]))

        
        for i in range(len(mat)):
            if i%2 != 0: 
                if not right_rotate(mat[i],k):
                    return False

            else: 
                if not left_rotate(mat[i],k):
                    return False

        return True


     



        


