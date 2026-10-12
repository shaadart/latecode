# Last updated: 12/10/2026, 07:46:27
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.min_stack = []
6        
7
8    def push(self, value: int) -> None:
9        self.stack.append(value)
10
11        if not self.min_stack:
12            self.min_stack.append(value)
13
14        else:
15            curr = min(value, self.min_stack[-1])
16            self.min_stack.append(curr)
17
18        
19
20    def pop(self) -> None:
21        self.stack.pop()
22        self.min_stack.pop()
23        
24
25    def top(self) -> int:
26        return self.stack[-1]
27
28        
29
30    def getMin(self) -> int:
31        return self.min_stack[-1]
32        
33
34
35# Your MinStack object will be instantiated and called as such:
36# obj = MinStack()
37# obj.push(value)
38# obj.pop()
39# param_3 = obj.top()
40# param_4 = obj.getMin()