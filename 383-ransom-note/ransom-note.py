class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = len(magazine)
        n = len(ransomNote)

        if m < n:
            return False

        magazine = list(magazine)

        for i in range(n):
            for j in range(len(magazine)):
                if ransomNote[i] == magazine[j]:
                    magazine.pop(j)   # use this character once
                    break
            else:
                # inner loop completed without finding a match
                return False

        return True