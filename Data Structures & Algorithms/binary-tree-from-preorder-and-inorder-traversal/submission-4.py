# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        tracker = {value:i for i,value in enumerate(inorder)}
        pre_index = 0
        def helper(left, right):
            nonlocal pre_index
            if left >= right:
                return
            branch = preorder[pre_index]
            pre_index += 1
            node = TreeNode(branch)
            mid = tracker[branch]
            node.left = helper(left, mid)
            node.right = helper(mid+1, right)
            return node
        return helper(0, len(inorder))