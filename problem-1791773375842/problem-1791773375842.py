# Last updated: 12/10/2026, 08:19:35
1class Solution:
2    def evalRPN(self, tokens: list[str]) -> int:
3        def compute(num1,o, num2):
4            if o == "+":
5                return str(int(num1)+int(num2))
6            if o == "-":
7                return str(int(num1)-int(num2))
8            if o == "/":
9                return str(int(int(num1) / int(num2)))
10            if o == "*":
11                return str(int(num1)*int(num2))
12        stk = []
13        for i in tokens:
14            if i not in ["+", "-", "*", "/"]:
15                stk.append(i)
16            
17            else:
18                c = compute(stk[-2], i, stk[-1])
19                #slice
20                stk.pop()
21                stk.pop()
22                stk.append(c)
23
24        return int(stk[0])
25                
26        