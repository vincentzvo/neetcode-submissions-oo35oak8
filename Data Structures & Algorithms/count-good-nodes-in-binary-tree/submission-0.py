# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        maxim = root.val

        def dfs(root, maxim):
            if not root:
                return None
            
            print(root.val)
            if root.val >= maxim:
                self.count += 1
                maxim = root.val
            
            dfs(root.left, maxim)
            dfs(root.right, maxim)
        
        dfs(root, maxim)
        return self.count