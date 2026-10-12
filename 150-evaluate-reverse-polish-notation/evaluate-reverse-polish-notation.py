class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def compute(num1,o, num2):
            if o == "+":
                return str(int(num1)+int(num2))
            if o == "-":
                return str(int(num1)-int(num2))
            if o == "/":
                return str(int(int(num1) / int(num2)))
            if o == "*":
                return str(int(num1)*int(num2))
        stk = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stk.append(i)
            
            else:
                c = compute(stk[-2], i, stk[-1])
                #slice
                stk.pop()
                stk.pop()
                stk.append(c)

        return int(stk[0])
                
        