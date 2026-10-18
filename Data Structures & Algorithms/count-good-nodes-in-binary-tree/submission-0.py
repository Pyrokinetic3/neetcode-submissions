# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 1
        def helper(root, max_val):
            nonlocal counter
            if not root:
                return
            if root.val >= max_val:
                counter += 1
                helper(root.left, root.val)
                helper(root.right, root.val)
            else:
                helper(root.left, max_val)
                helper(root.right, max_val)
        helper(root.right, root.val)
        helper(root.left, root.val)
        return counter