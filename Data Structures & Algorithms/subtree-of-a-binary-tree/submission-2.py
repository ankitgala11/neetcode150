# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(node):
            if not node:
                return "()"
            left = serialize(node.left)
            right = serialize(node.right)

            return "(" + left + ")" +str(node.val) + "(" + right + ")"

        sub = serialize(subRoot)

        # Check all subtrees
        def check(node):
            if not node:
                return "()"

            left = check(node.left)
            right = check(node.right)

            curr = "(" + left + ")" +str(node.val) + "(" + right + ")"

            if curr == sub:
                self.found = True

            return curr

        self.found = False
        check(root)
        return self.found