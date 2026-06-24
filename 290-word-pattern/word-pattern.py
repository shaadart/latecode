class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        out = {}
        pattern = list(pattern)
        s = s.split()

        if len(pattern) != len(s):
            return False

        # build output
        for i in range(len(pattern)):
            if pattern[i] in out:
                if out[pattern[i]] != s[i]:
                    return False

            elif s[i] in out.values():
                return False

            else:
                out[pattern[i]] = s[i]

        return True
