# Last updated: 3/27/2026, 2:40:04 PM
1
2class Solution:
3    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
4        def isMirror(t1, t2):
5            if not t1 and not t2: 
6                return True
7            if not t1 or not t2:
8                return False
9
10            return(t1.val == t2.val and 
11            isMirror(t1.left, t2.right) and 
12            isMirror(t1.right, t2.left) 
13            )
14
15        return isMirror(root.left, root.right)
16
17
18        