# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(root1, root2):
            flag = [True]
            def compare(p, q):
                if not p and not q:
                    return
                if not p or not q:
                    flag[0] = False
                    return
                if p.val != q.val:
                    flag[0] = False
                    return
                l1 = p.left
                l2 = q.left
                r1 = p.right
                r2 = q.right
                compare(l1, l2)
                compare(r1, r2)
            compare(root1, root2)
            return flag[0]
        
        def search(root):
            if not root:
                return False
            return (same_tree(root, subRoot) or search(root.left) or search(root.right))
        if not subRoot:
            return True
        return search(root)