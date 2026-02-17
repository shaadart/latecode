class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        
        for i in range (12): 
            for j in range (60):

                if (bin(i).count('1') + bin(j).count('1')) == turnedOn:
                    time = f"{i}:{j:02}"
                    res.append(time)

        return res