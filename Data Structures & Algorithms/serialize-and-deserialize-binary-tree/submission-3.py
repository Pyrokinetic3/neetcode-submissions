# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        max_depths = []
        def max_depth_finder(root, depth):
            if not root:
                return
            max_depths.append(depth)
            max_depth_finder(root.left, depth+1)
            max_depth_finder(root.right, depth+1)
        max_depth_finder(root, 0)
        max_depth = max(max_depths)
        output = [[] for i in range(max_depth+1)]
        def filler(root, depth):
            if not root and depth <= max_depth:
                output[depth].append(None)
                return
            elif not root:
                return
            output[depth].append(root.val)
            filler(root.left, depth+1)
            filler(root.right, depth+1)
        filler(root, 0)
        str_output = str(output)[1:-1]
        str_output = str_output.replace(' ', '')
        return str_output
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return
        root_end = data.index(']')
        output = [[int(data[1:root_end])]]
        i = root_end + 1
        d = 0
        while i < len(data):
            if data[i] == '[':
                output.append([])
                d += 1
                j = i + 1
            if data[i] == ']':
                if data[j:i] == 'None':
                    output[d].append('None')
                else:
                    output[d].append(int(data[j:i]))                
                i += 1
                j = i + 1
            i += 1
            if i < len(data) and data[i] == ',':
                if data[j:i] == 'None':
                    output[d].append('None')
                else:
                    output[d].append(int(data[j:i]))
                j = i + 1
        root = TreeNode(output[0][0])
        parents = [root]        
        def builder(parents, depth):
            if depth >= len(output):
                return
            counter = 0
            next_parents = []
            for parent in parents:
                left_value = output[depth][counter]
                right_value = output[depth][counter + 1]
                counter += 2
                if left_value != 'None':
                    parent.left = TreeNode(left_value)
                    next_parents.append(parent.left)
                if right_value != 'None':
                    parent.right = TreeNode(right_value)
                    next_parents.append(parent.right)
            builder(next_parents, depth + 1)
        builder(parents, 1)
        return root