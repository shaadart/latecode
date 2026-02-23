class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:


        seen = set()

        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])

        return len(seen) == 2 **k
        # um = []
        # for i in range(0,len(s)-k+1):
        #     temp = []
        #     for j in range(i,k+i):
                
        #         temp.append(s[j])
        #     if temp not in um:
        #         um.append(temp)

        # if len(um) == 2**k:
        #     return True
        # else: 
        #     return False





        