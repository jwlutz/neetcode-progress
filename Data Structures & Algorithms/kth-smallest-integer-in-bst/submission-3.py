# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.cnt = 0

        def dfs(root):
            if root:
                dfs(root.left)
                self.cnt += 1
                if self.cnt == k:
                    self.ans = root.val
                dfs(root.right)
        dfs(root)
        return self.ans