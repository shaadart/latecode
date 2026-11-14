class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"}":"{", ")":"(", "]":"[" }

        for i in s:
            if i in list(brackets.values()):
                stack.append(i)

            elif i in list(brackets.keys()):
                if not stack:
                    return False
                
                if brackets[i]!=stack[-1]:
                    return False
                
                stack.pop(-1)
                

        
        return len(stack)==0