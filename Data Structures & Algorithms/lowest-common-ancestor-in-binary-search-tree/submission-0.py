# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #do DFS
        if not root:
            return None
        if p.val == q.val:
            return p

        #recurse while both p.val and q.val >= or <= root.val
        def dfs(root, p, q):
            if root.val > p.val and root.val > q.val:
                if not root.left:
                    return root
                return dfs(root.left, p, q)
            elif root.val < p.val and root.val < q.val:
                if not root.right:
                    return root
                return dfs(root.right, p, q)
            else:
                return root

        return dfs(root, p, q)