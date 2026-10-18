# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        max_depths = []
        def max_depth(root, depth):
            if not root:
                max_depths.append(depth)
                return
            max_depth(root.left, depth+1)
            max_depth(root.right, depth+1)
        max_depth(root, 0)
        output = [[] for i in range(max(max_depths))]
        def helper(root, depth):
            if not root:
                return
            output[depth].append(root.val)
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        helper(root, 0)
        return output
        