# Last updated: 5/8/2026, 6:48:12 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9
10        ans=[]
11        def preorder(root):
12            if root is None:
13                return
14
15            ans.append(root.val)
16            preorder(root.left)
17            preorder(root.right)
18            
19
20        preorder(root)
21        return ans
22
23
24        