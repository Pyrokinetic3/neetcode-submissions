# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depths = []
        def helper(root, depth):
            if not root:
                max_depths.append(depth)
            else:
                roots = [root.left, root.right]
                for i in roots:
                    helper(i, depth+1)
        if not root:
            return 0
        helper(root, 0)
        return max(max_depths)