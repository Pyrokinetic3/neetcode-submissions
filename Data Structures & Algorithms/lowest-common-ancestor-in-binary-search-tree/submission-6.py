# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
             q, p = p, q
        def helper(root0):
            if p.val <= root0.val and q.val >= root0.val:
                return root0
            if p.val <= root0.val and q.val <= root0.val:
                return helper(root0.left)
            if p.val >= root0.val and q.val >= root0.val:
                return helper(root0.right)
        return helper(root)