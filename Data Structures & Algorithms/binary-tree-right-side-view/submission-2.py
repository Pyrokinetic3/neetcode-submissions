# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = [root.val]
        def helper(root, depth):
            if not root:
                return
            if depth == len(output):
                output.append(root.val)
            helper(root.right, depth+1)
            helper(root.left, depth+1)
        helper(root.right, 1)
        helper(root.left, 1)
        return output