class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = chr(ord(s[i-1])+ int(s[i])) #i-1 is because we are checking "a" i.e before number

        return "".join(s)
        