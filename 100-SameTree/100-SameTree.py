# Last updated: 04/09/2026, 07:11:02
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        res1 = []
10        res2 = []
11
12        def solve(root, res):
13            if not root:
14                res.append(None)
15                return res
16
17            res.append(root.val)
18            solve(root.left,res)
19            solve(root.right,res)
20            return res
21
22        return solve(p, res1) == solve(q,res2)