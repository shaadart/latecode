class Solution:
    def isValid(self, s: str) -> bool:
        #defination
        stack = []
        bracketmap = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in "([{":
                stack.append(ch)

            else:
                if not stack:
                    return False

                if stack.pop() != bracketmap[ch]:
                    return False


        return len(stack) == 0