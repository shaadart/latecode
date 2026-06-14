class Solution:
    def isValid(self, s: str) -> bool:
        #defination
        stack = []
        rev_bracket_map = {")": "(", "}": "{", "]": "["}


        spl = list(s)


        for i in spl:
            #opening: push

            if i in ["(", "[", "{"]:
                stack.append(i)

            #closing:

            elif i in [")", "]", "}"]:
                if not stack:
                    return False

                else: 
                    if stack[-1] == rev_bracket_map[i]:
                        stack.pop()
                    else:
                        return False

        return len(stack) == 0





        
        
