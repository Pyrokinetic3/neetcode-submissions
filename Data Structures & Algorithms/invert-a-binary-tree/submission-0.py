# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def is_leaf(root):
            if not root:
                return False
            elif not root.left and not root.right:
                return True
            else:
                return False
        def helper(root):
            if not root:
                return False
            if is_leaf(root):
                return
            root.left, root.right = root.right, root.left
            roots = [root.left, root.right]
            for i in roots:
                helper(i)
        helper(root)
        return root