# Last updated: 04/09/2026, 14:52:36
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDepth(self, root: Optional[TreeNode]) -> int:
9
10        def dfs(node):
11            if not node: 
12                return 0
13
14            left = dfs(node.left)
15            right = dfs(node.right)
16
17            if not node.left: 
18                return 1+right
19            
20            if not node.right: 
21                return 1+left
22
23            return 1 + min(left , right)
24
25        return dfs(root)
26
27        