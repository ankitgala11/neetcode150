# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return [0, 0]
            
            op1 = solve(root.left)
            op2 = solve(root.right)
            op3 = op1[1] + op2[1]

            return [max(op1[0], op2[0], op3) , max(op1[1], op2[1]) + 1]

        return solve(root)[0]

        # def height(root):
        #     if not root:
        #         return 0

        #     return max(height(root.left) , height(root.right)) + 1

        # def solve(root):
        #     if not root:
        #         return 0

        #     op1 = solve(root.left)
        #     op2 = solve(root.right)
        #     op3 = (height(root.left) + height(root.right)) 

        
        #     return max(op1, op2, op3)
        
        # return solve(root)

            