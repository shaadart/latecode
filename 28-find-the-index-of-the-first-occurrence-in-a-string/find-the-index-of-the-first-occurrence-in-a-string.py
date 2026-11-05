class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        n = len(haystack)
        while i < n:
            window = haystack[i:i+len(needle)]

            if needle == window:
                return i

            i+=1

        return -1
