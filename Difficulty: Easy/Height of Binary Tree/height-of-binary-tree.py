class Solution:
    def height(self, root):
        if root is None:
            return -1  # Returns height based on edges rather than nodes
        return 1 + max(self.height(root.left), self.height(root.right))
