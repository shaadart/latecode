# Last updated: 03/09/2026, 16:08:36
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10        def inorder(root):
11            if not root:
12                return 
13            
14            inorder(root.left)
15            res.append(root.val)
16            inorder(root.right)
17
18        inorder(root)
19        return res
20        