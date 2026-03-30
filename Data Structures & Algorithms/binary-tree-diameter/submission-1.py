# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, cur):
        if not cur:
            return 0

        left = self.dfs(cur.left)
        right = self.dfs(cur.right)

        self.res = max(self.res, left + right)
        return 1 + max(left, right)