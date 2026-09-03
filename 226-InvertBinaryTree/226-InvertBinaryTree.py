# Last updated: 03/09/2026, 17:00:25
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        
10        if not root:
11            return None
12
13        root.left ,root.right = root.right, root.left
14        self.invertTree(root.left)
15        self.invertTree(root.right)
16
17        return root
18        
19
20        
21        