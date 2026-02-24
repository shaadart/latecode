# Last updated: 2/24/2026, 8:27:08 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
9
10        def sumRootToLeaf(root, sum):
11            if root == None: return 0
12            sum = (sum << 1) + root.val
13            if root.left == None and root.right == None: 
14                return sum
15
16            return sumRootToLeaf(root.left, sum) + sumRootToLeaf(root.right, sum)
17
18        return sumRootToLeaf(root, 0)
19        