# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = [True]
        def helper(root, upper, lower):
            if not root:
                return
            if not (lower < root.val < upper):
                flag[0] = False
                return
            helper(root.left, root.val, lower)
            helper(root.right, upper, root.val)
        helper(root, float('inf'), float('-inf'))
        return flag[0]