class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seeni = {}
        seenj = {}

        for i in s: 
            seeni[i] = seeni.get(i, 0)+1

        for j in t: 
            seenj[j] = seenj.get(j, 0)+1

        return seenj == seeni

        

        