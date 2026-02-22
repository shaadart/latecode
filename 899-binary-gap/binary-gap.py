class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]   
        
        max_dist = 0
        last_index = -1
        
        for i in range(len(binary)):
            if binary[i] == '1':
                if last_index != -1:
                    max_dist =  max(i-last_index, max_dist)

                last_index = i

        return max_dist
                    
                