# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []

        def solve(root, res):
            if not root:
                res.append(None)
                return res

            res.append(root.val)
            solve(root.left,res)
            solve(root.right,res)
            return res

        return solve(p, res1) == solve(q,res2)