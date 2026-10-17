# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = [True]
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            if abs(l - r) > 1:
                flag[0] = False
            return 1 + max(l, r)
        helper(root)
        return flag[0]