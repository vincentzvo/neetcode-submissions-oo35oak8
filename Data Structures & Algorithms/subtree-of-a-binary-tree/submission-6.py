# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        res = False

        while stack:
            node = stack.pop()
            if node:
                if node.val == subRoot.val:
                    res = res or self.isSameTree(node, subRoot)
                stack.append(node.left)
                stack.append(node.right)
        return res
            
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and not q or not p and q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)