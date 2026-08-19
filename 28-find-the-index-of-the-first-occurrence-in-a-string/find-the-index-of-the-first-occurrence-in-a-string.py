class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < (len(haystack)):
            window = haystack[i:i+len(needle)]
            # print(window)

            if needle == window:
                return i
            i+=1

        return -1
