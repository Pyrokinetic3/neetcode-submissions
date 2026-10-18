# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        def helper(root):
            if not root:
                return
            nodes.append(root.val)
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
        helper(root)
        nodes = sorted(nodes)
        return nodes[k-1]
