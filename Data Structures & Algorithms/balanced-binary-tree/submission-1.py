# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def solve(root):

            if not root:
                return [True, 0]

            left = solve(root.left)
            right = solve(root.right)

            a = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            b = max(left[1], right[1]) + 1
            return [a , b]
        
        return solve(root)[0]
        