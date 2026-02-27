# Last updated: 2/27/2026, 2:57:43 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        
10        if not root or root.val == val:
11            return root
12
13        if root.val > val:
14            return self.searchBST(root.left, val)
15
16        return self.searchBST(root.right, val)