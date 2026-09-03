# Last updated: 03/09/2026, 16:03:50
1class Solution:
2    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
3        res = []
4        
5        def dfs(node):
6            if not node:
7                return
8            res.append(node.val)  
9            dfs(node.left)        
10            dfs(node.right) 
11            
12        dfs(root)
13        return res
14