# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def solve(root, maxi, mini):

            if not root:
                return True

            if root.val<=mini or root.val>=maxi:
                return False
            
            return solve(root.left, root.val, mini) and solve(root.right, maxi, root.val)
       

        
        return solve(root, float('inf'), float('-inf'))

        