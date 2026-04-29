# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def solve(root):
            if not root:
                return None
            
            if root.val == p.val or root.val == q.val:
                return root

            left = solve(root.left)
            right = solve(root.right)

            if left and right:
                return root

            elif left and not right:
                return left
            
            else :
                return right

        return solve(root)