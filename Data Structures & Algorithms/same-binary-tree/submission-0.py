# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = [True]
        def helper(root1, root2):
            if not root1 and not root2:
                return
            if not root1 or not root2:
                flag[0] = False
                return
            if root1.val != root2.val:
                flag[0] = False
                return
            l1 = root1.left
            l2 = root2.left
            r1 = root1.right
            r2 = root2.right
            helper(l1, l2)
            helper(r1, r2)
        helper(p, q)
        return flag[0]