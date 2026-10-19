# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        output = []
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            output.append(max(0, l) + root.val + max(0, r))
            return root.val + max(0, l, r)
        helper(root)
        return max(output)