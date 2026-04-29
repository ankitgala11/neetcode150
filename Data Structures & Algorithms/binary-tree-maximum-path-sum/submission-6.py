# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = float('-inf')
        curr = float('-inf')


        def solve(root):
            nonlocal res, curr

            if not root:
                return 0

            left = solve(root.left)
            right = solve(root.right)


            curr = left + root.val + right

            res = max(res, curr, root.val, left + root.val, right + root.val)

            return max(left + root.val, right + root.val, root.val)

            

        
        solve(root)
        return res
        