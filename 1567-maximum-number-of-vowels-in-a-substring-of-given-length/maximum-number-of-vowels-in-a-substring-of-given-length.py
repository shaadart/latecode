class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        n = len(s)

        ans = 0
        count = 0


        for i in range(k):
            if s[i] in "aeiou":
                count += 1

        ans = count

        for j in range(k, n):
            if s[j] in "aeiou":
                count += 1

            if s[j - k] in "aeiou":
                count -= 1

            ans = max(count, ans)

        return ans
