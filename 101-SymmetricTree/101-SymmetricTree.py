# Last updated: 04/09/2026, 14:41:30
1
2class Solution:
3    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
4        def ismirror(a,b):
5            if not a and not b:
6                return True
7            
8            if not a or not b: 
9                return False
10
11            if a.val != b.val:
12                return False
13
14            return (ismirror(a.left, b.right) and ismirror(a.right, b.left))
15
16        return ismirror(root.left, root.right)
17
18        