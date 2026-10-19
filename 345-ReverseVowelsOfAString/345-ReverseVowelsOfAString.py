# Last updated: 19/10/2026, 16:27:38
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)  # convert string to list for swapping
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]  # swap vowels
                i += 1
                j -= 1
            elif s[i] not in vowels:
                i += 1
            else:
                j -= 1

        return "".join(s)  # convert back to string
