# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_level = 0

        def dfs(root, level):
            if root:
                dfs(root.left, level + 1)
                if level > self.max_level:
                    self.max_level = level
                dfs(root.right, level + 1)
        dfs(root, 1)
        return self.max_level
                