# Last updated: 03/09/2026, 16:40:53
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        def depth(root):
10            if not root: 
11                return 0
12            
13            left = depth(root.left)
14            right = depth(root.right)
15            return 1 + max(left, right)
16
17        return depth(root)
18
19        