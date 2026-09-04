# Last updated: 04/09/2026, 14:46:08
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        
10        def invert(root):
11            if not root:
12                return None
13
14            root.left, root.right = (invert(root.right), invert(root.left))
15        
16            return root
17
18        return invert(root)
19        
20        