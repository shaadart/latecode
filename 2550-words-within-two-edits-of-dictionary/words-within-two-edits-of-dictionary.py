class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        
        for q in range(len(queries)):
            for d in range(len(dictionary)):
                diff = 0
                
                for j in range(len(queries[0])):
                    if queries[q][j] != dictionary[d][j]:
                        diff += 1
                        if diff > 2:
                            break
                
                if diff <= 2:
                    res.append(queries[q])
                    break        
        return res