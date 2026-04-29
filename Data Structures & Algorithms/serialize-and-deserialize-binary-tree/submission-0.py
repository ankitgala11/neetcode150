# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        if not root:
            return ""
        q = [root]
        while q:
            node = q.pop(0)
            if node == "N":
                data.append("N,")
                continue
            data.append(str(node.val)+",")
            if node.left:q.append(node.left)
            else:q.append("N")
            if node.right:q.append(node.right)
            else:q.append("N")
        
        return "".join(data)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")[:-1]
        # print(vals)
        if not vals:
            return None
        root = TreeNode(int(vals[0]))
        q = [root]
        i = 1
        while q and i < len(vals):
            node = q.pop(0)
            if vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root


        




