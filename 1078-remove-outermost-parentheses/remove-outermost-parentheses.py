class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, lvl = [], 0
        for b in s:
            if b == ")":
                lvl -= 1 

            if lvl>0:
                res.append(b)
            if b == "(":
                lvl +=1

        return "".join(res) 

        