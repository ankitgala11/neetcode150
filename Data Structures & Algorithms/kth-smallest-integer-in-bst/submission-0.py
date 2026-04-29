# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # maxh = []

        def solve(root):
            nonlocal cnt, ans
            if not root:return

            if root.left:
                solve(root.left)
            
            cnt += 1
            if cnt == k:
                ans = root.val
            
            if root.right:
                solve(root.right)
            
        cnt = 0
        ans = 0

        solve(root)
        return ans