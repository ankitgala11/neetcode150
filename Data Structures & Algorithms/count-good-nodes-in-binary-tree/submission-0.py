# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans = 0

        def solve(root, maxi):
            nonlocal ans

            if not root:
                return None

            if maxi<=root.val:
                ans += 1

            if root.left:solve(root.left, max(maxi, root.left.val))
            if root.right:solve(root.right, max(maxi, root.right.val))


        solve(root, root.val)
        return ans
            

        