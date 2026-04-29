# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        def solve(inS, inE):
            nonlocal preIdx

            if preIdx >= n or inS>inE:
                return

            ele = preorder[preIdx]
            node = TreeNode(ele)
            preIdx += 1
            inIdx = -1

            for i in range(inS, inE+1):
                if inorder[i] == ele:
                    inIdx = i
                    break
            
            if inIdx != -1:
                node.left = solve(inS, inIdx-1)
                node.right = solve(inIdx+1, inE)

            return node

        preIdx = 0
        return solve(0, n-1)




