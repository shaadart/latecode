class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:

        evenMatch = sorted(s1[::2]) == sorted(s2[::2])
        oddMatch = sorted(s1[1::2]) == sorted(s2[1::2])
        return evenMatch and oddMatch
        